class FileExplorer {
    constructor() {
        this.currentPath = './';
        this.init();
    }
 
    init() {
        this.bindEvents();
        this.loadFiles();
    }
 
    bindEvents() {
        // Navegação
        document.getElementById('fileList').addEventListener('click', (e) => {
            const row = e.target.closest('tr');
            if (row && row.dataset.path) {
                if (row.dataset.isDirectory === 'true') {
                    this.navigateTo(row.dataset.path);
                } else {
                    this.viewFile(row.dataset.path, row.dataset.name);
                }
            }
        });
 
        // Botões de ação
        document.getElementById('btnNewFolder').addEventListener('click', () => this.showNewFolderModal());
        document.getElementById('btnUpload').addEventListener('click', () => document.getElementById('fileInput').click());
        document.getElementById('fileInput').addEventListener('change', (e) => this.uploadFiles(e.target.files));
 
        // Modal nova pasta
        document.getElementById('btnCreateFolder').addEventListener('click', () => this.createFolder());
        document.getElementById('btnCancelFolder').addEventListener('click', () => this.hideModal('folderModal'));
        document.getElementById('folderName').addEventListener('keypress', (e) => {
            if (e.key === 'Enter') this.createFolder();
        });
 
        // Modal arquivo
        document.getElementById('btnCloseFile').addEventListener('click', () => this.hideModal('fileModal'));
 
        // Navegação pelo breadcrumb (simplificada)
        document.querySelector('.breadcrumb').addEventListener('click', () => {
            this.navigateToUp();
        });
    }
 
    async loadFiles(path = this.currentPath) {
        this.showLoading();
        this.hideError();
 
        try {
            const response = await fetch(`/api/files?path=${encodeURIComponent(path)}`);
            const data = await response.json();
 
            if (data.success) {
                this.currentPath = data.currentPath;
                this.displayFiles(data.files, data.parentPath);
                this.updateBreadcrumb(data.currentPath);
            } else {
                this.showError(data.error);
            }
        } catch (error) {
            this.showError('Erro ao carregar arquivos: ' + error.message);
        } finally {
            this.hideLoading();
        }
    }
 
    displayFiles(files, parentPath) {
        const tbody = document.getElementById('fileList');
        tbody.innerHTML = '';
 
        // Adicionar link para pasta pai se não for a raiz
        if (parentPath && parentPath !== this.currentPath) {
            const parentRow = this.createFileRow({
                name: '..',
                path: parentPath,
                isDirectory: true,
                size: null,
                modified: null,
                permissions: 'rwx'
            }, true);
            tbody.appendChild(parentRow);
        }
 
        files.forEach(file => {
            const row = this.createFileRow(file);
            tbody.appendChild(row);
        });
    }
 
    createFileRow(file, isParent = false) {
        const row = document.createElement('tr');
        row.className = 'file-item';
        row.dataset.path = file.path;
        row.dataset.isDirectory = file.isDirectory;
        row.dataset.name = file.name;
 
        const nameCell = document.createElement('td');
        nameCell.className = 'file-name';
        nameCell.innerHTML = `
            <span class="${file.isDirectory ? 'folder-icon' : 'file-icon'}">
                ${file.isDirectory ? '📁' : '📄'}
            </span>
            ${file.name}
        `;
 
        const sizeCell = document.createElement('td');
        sizeCell.textContent = file.isDirectory ? '-' : this.formatFileSize(file.size);
 
        const modifiedCell = document.createElement('td');
        modifiedCell.textContent = file.modified ? new Date(file.modified).toLocaleString() : '-';
 
        const permCell = document.createElement('td');
        permCell.textContent = file.permissions || '-';
 
        const actionsCell = document.createElement('td');
        actionsCell.className = 'file-actions';
        
        if (!isParent) {
            actionsCell.innerHTML = `
                <button class="btn btn-secondary" onclick="event.stopPropagation(); explorer.renameItem('${file.path}', '${file.name}')">Renomear</button>
                <button class="btn btn-danger" onclick="event.stopPropagation(); explorer.deleteItem('${file.path}')">Deletar</button>
            `;
        }
 
        row.appendChild(nameCell);
        row.appendChild(sizeCell);
        row.appendChild(modifiedCell);
        row.appendChild(permCell);
        row.appendChild(actionsCell);
 
        return row;
    }
 
    navigateTo(path) {
        this.loadFiles(path);
    }
 
    navigateToUp() {
        const parentPath = path.dirname(this.currentPath);
        if (parentPath !== this.currentPath) {
            this.loadFiles(parentPath);
        }
    }
 
    showNewFolderModal() {
        document.getElementById('folderName').value = '';
        this.showModal('folderModal');
    }
 
    async createFolder() {
        const name = document.getElementById('folderName').value.trim();
        
        if (!name) {
            alert('Por favor, digite um nome para a pasta');
            return;
        }
 
        try {
            const response = await fetch('/api/folder', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    path: this.currentPath,
                    name: name
                })
            });
 
            const data = await response.json();
 
            if (data.success) {
                this.hideModal('folderModal');
                this.loadFiles();
            } else {
                alert('Erro: ' + data.error);
            }
        } catch (error) {
            alert('Erro ao criar pasta: ' + error.message);
        }
    }
 
    async uploadFiles(fileList) {
        if (fileList.length === 0) return;
 
        const formData = new FormData();
        formData.append('currentPath', this.currentPath);
        
        for (let i = 0; i < fileList.length; i++) {
            formData.append('files', fileList[i]);
        }
 
        try {
            const response = await fetch('/api/upload', {
                method: 'POST',
                body: formData
            });
 
            const data = await response.json();
 
            if (data.success) {
                alert(data.message);
                this.loadFiles();
            } else {
                alert('Erro: ' + data.error);
            }
        } catch (error) {
            alert('Erro no upload: ' + error.message);
        }
 
        // Limpar input
        document.getElementById('fileInput').value = '';
    }
 
    async deleteItem(itemPath) {
        if (!confirm('Tem certeza que deseja deletar este item?')) return;
 
        try {
            const response = await fetch('/api/delete', {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    path: itemPath
                })
            });
 
            const data = await response.json();
 
            if (data.success) {
                this.loadFiles();
            } else {
                alert('Erro: ' + data.error);
            }
        } catch (error) {
            alert('Erro ao deletar: ' + error.message);
        }
    }
 
    async renameItem(oldPath, oldName) {
        const newName = prompt('Novo nome:', oldName);
        
        if (!newName || newName === oldName) return;
 
        try {
            const response = await fetch('/api/rename', {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    oldPath: oldPath,
                    newName: newName
                })
            });
 
            const data = await response.json();
 
            if (data.success) {
                this.loadFiles();
            } else {
                alert('Erro: ' + data.error);
            }
        } catch (error) {
            alert('Erro ao renomear: ' + error.message);
        }
    }
 
    async viewFile(filePath, fileName) {
        try {
            const response = await fetch(`/api/file-content?path=${encodeURIComponent(filePath)}`);
            const data = await response.json();
 
            if (data.success) {
                document.getElementById('fileName').textContent = fileName;
                document.getElementById('fileContent').textContent = data.content;
                this.showModal('fileModal');
            } else {
                alert('Erro: ' + data.error);
            }
        } catch (error) {
            alert('Erro ao carregar arquivo: ' + error.message);
        }
    }
 
    updateBreadcrumb(currentPath) {
        document.getElementById('currentPath').textContent = currentPath;
    }
 
    formatFileSize(bytes) {
        if (bytes === 0) return '0 B';
        const k = 1024;
        const sizes = ['B', 'KB', 'MB', 'GB'];
        const i = Math.floor(Math.log(bytes) / Math.log(k));
        return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
    }
 
    showModal(modalId) {
        document.getElementById(modalId).style.display = 'block';
    }
 
    hideModal(modalId) {
        document.getElementById(modalId).style.display = 'none';
    }
 
    showLoading() {
        document.getElementById('loading').style.display = 'block';
    }
 
    hideLoading() {
        document.getElementById('loading').style.display = 'none';
    }
 
    showError(message) {
        const errorDiv = document.getElementById('error');
        errorDiv.textContent = message;
        errorDiv.style.display = 'block';
    }
 
    hideError() {
        document.getElementById('error').style.display = 'none';
    }
}
 
// Inicializar o explorador quando a página carregar
const explorer = new FileExplorer();
 