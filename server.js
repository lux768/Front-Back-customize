const express = require('express');
const fs = require('fs');
const path = require('path');
const cors = require('cors');
const multer = require('multer');
 
const app = express();
const PORT = 3000;
 
// Middleware
app.use(cors());
app.use(express.json());
app.use(express.static('public'));
app.use(express.urlencoded({ extended: true }));
 
// Configuração do multer para upload de arquivos
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    const currentPath = path.resolve(req.body.currentPath || './');
    cb(null, currentPath);
  },
  filename: (req, file, cb) => {
    cb(null, file.originalname);
  }
});
 
const upload = multer({ storage });
 
// Função para listar arquivos e pastas
function listDirectory(dirPath) {
  try {
    const absolutePath = path.resolve(dirPath);
    
    // Verificar se o diretório existe
    if (!fs.existsSync(absolutePath)) {
      throw new Error('Diretório não existe');
    }
 
    const items = fs.readdirSync(absolutePath);
    const result = [];
 
    for (const item of items) {
      const itemPath = path.join(absolutePath, item);
      const stats = fs.statSync(itemPath);
      
      result.push({
        name: item,
        path: itemPath,
        isDirectory: stats.isDirectory(),
        size: stats.isDirectory() ? null : stats.size,
        modified: stats.mtime,
        permissions: getPermissions(stats)
      });
    }
 
    // Ordenar: pastas primeiro, depois arquivos
    result.sort((a, b) => {
      if (a.isDirectory && !b.isDirectory) return -1;
      if (!a.isDirectory && b.isDirectory) return 1;
      return a.name.localeCompare(b.name);
    });
 
    return result;
  } catch (error) {
    throw new Error(`Erro ao ler diretório: ${error.message}`);
  }
}
 
// Função auxiliar para obter permissões (simplificada)
function getPermissions(stats) {
  const perms = [];
  if (stats.mode & 0o400) perms.push('r');
  if (stats.mode & 0o200) perms.push('w');
  if (stats.mode & 0o100) perms.push('x');
  return perms.join('');
}
 
// Rotas da API
 
// Listar conteúdo do diretório
app.get('/api/files', (req, res) => {
  const { path: dirPath = './' } = req.query;
  try {
    const files = listDirectory(dirPath);
    const currentDir = path.resolve(dirPath);
    res.json({
      success: true,
      currentPath: currentDir,
      files: files,
      parentPath: path.dirname(currentDir)
    });
  } catch (error) {
    res.status(400).json({
      success: false,
      error: error.message
    });
  }
});
 
// Criar nova pasta
app.post('/api/folder', (req, res) => {
  const { path: folderPath, name } = req.body;
  
  try {
    const fullPath = path.join(folderPath, name);
    
    if (fs.existsSync(fullPath)) {
      return res.status(400).json({
        success: false,
        error: 'Já existe uma pasta com este nome'
      });
    }
    
    fs.mkdirSync(fullPath, { recursive: true });
    
    res.json({
      success: true,
      message: 'Pasta criada com sucesso'
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: error.message
    });
  }
});
 
// Upload de arquivos
app.post('/api/upload', upload.array('files'), (req, res) => {
  try {
    res.json({
      success: true,
      message: `${req.files.length} arquivo(s) enviado(s) com sucesso`
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: error.message
    });
  }
});
 
// Deletar arquivo ou pasta
app.delete('/api/delete', (req, res) => {
  const { path: itemPath } = req.body;
  
  try {
    const fullPath = path.resolve(itemPath);
    
    if (!fs.existsSync(fullPath)) {
      return res.status(404).json({
        success: false,
        error: 'Arquivo ou pasta não encontrado'
      });
    }
    
    const stats = fs.statSync(fullPath);
    
    if (stats.isDirectory()) {
      fs.rmdirSync(fullPath, { recursive: true });
    } else {
      fs.unlinkSync(fullPath);
    }
    
    res.json({
      success: true,
      message: 'Item deletado com sucesso'
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: error.message
    });
  }
});
 
// Renomear arquivo ou pasta
app.put('/api/rename', (req, res) => {
  const { oldPath, newName } = req.body;
  
  try {
    const fullOldPath = path.resolve(oldPath);
    const directory = path.dirname(fullOldPath);
    const fullNewPath = path.join(directory, newName);
    
    if (!fs.existsSync(fullOldPath)) {
      return res.status(404).json({
        success: false,
        error: 'Arquivo ou pasta não encontrado'
      });
    }
    
    if (fs.existsSync(fullNewPath)) {
      return res.status(400).json({
        success: false,
        error: 'Já existe um item com este nome'
      });
    }
    
    fs.renameSync(fullOldPath, fullNewPath);
    
    res.json({
      success: true,
      message: 'Item renomeado com sucesso'
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: error.message
    });
  }
});
 
// Visualizar conteúdo de arquivo de texto
app.get('/api/file-content', (req, res) => {
  const { path: filePath } = req.query;
  
  try {
    const fullPath = path.resolve(filePath);
    
    if (!fs.existsSync(fullPath)) {
      return res.status(404).json({
        success: false,
        error: 'Arquivo não encontrado'
      });
    }
    
    const stats = fs.statSync(fullPath);
    if (stats.isDirectory()) {
      return res.status(400).json({
        success: false,
        error: 'O caminho especificado é uma pasta'
      });
    }
    
    // Verificar se é um arquivo de texto (por extensão)
    const textExtensions = ['.txt', '.js', '.html', '.css', '.json', '.xml', '.md'];
    const ext = path.extname(fullPath).toLowerCase();
    
    if (!textExtensions.includes(ext)) {
      return res.status(400).json({
        success: false,
        error: 'Tipo de arquivo não suportado para visualização'
      });
    }
    
    const content = fs.readFileSync(fullPath, 'utf8');
    
    res.json({
      success: true,
      content: content,
      size: stats.size
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: error.message
    });
  }
});
 
// Iniciar servidor
app.listen(PORT, () => {
  console.log(`Servidor rodando em http://localhost:${PORT}`);
  console.log(`Navegador de arquivos disponível em http://localhost:${PORT}/api/files`);
});
