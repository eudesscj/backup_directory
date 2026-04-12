# 📦 Backup Script

Script Python para compactar um diretório de origem em `.zip` e mover o arquivo para um destino final, passando por um diretório temporário.

## ⚙️ Funcionalidades

- Compacta um diretório inteiro em `.zip`
- Remove backup anterior automaticamente se existir
- Usa diretório temporário para evitar gravação direta no destino
- Exibe o tempo de execução de cada etapa e o total

## 🛠️ Pré-requisitos

- Python 3.x
- Apenas bibliotecas nativas (`os`, `shutil`, `time`, `datetime`)

## 🚀 Como usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/SEU_USUARIO/NOME_DO_REPO.git
   ```

2. Edite as variáveis de configuração no início do script:
   ```python
   source_directory = r"C:\caminho\origem"
   destination_directory = r"C:\caminho\destino"
   temp_directory = r"C:\caminho\temp"
   zip_temp = os.path.join(temp_directory, "nome_do_arquivo")
   ```

3. Execute:
   ```bash
   python backup.py
   ```

## 📁 Estrutura esperada

```
backup-script/
│
├── backup.py       # Script principal
└── README.md       # Documentação
```

## 📌 Observações

- O diretório temporário é removido automaticamente ao final da execução.
- Se o `.zip` já existir no destino, ele será substituído.
- Em caso de erro, a mensagem será exibida no console.
