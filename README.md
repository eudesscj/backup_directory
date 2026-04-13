# 📦 Backup Script

Script Python para compactar um diretório de origem em `.zip` com timestamp, mover o arquivo para um destino final e gerenciar o histórico de backups automaticamente.

---

## ⚙️ Funcionalidades

- Compacta um diretório inteiro em `.zip`
- Nomeia o arquivo com data e hora — ex: `Backup_Ger_Inteligencia_20240415_143022.zip`
- Valida a integridade do ZIP gerado (existência e tamanho)
- Move o ZIP para o diretório de destino
- Remove backups antigos automaticamente, mantendo apenas os N mais recentes
- Registra toda a execução em arquivo `.log` e no console simultaneamente
- Garante limpeza do diretório temporário mesmo em caso de erro

---

## 🛠️ Pré-requisitos

- Python 3.8+
- Apenas bibliotecas nativas (`os`, `shutil`, `time`, `datetime`, `logging`, `pathlib`)

---

## 🚀 Como usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/SEU_USUARIO/NOME_DO_REPO.git
   ```

2. Configure as variáveis no início do script:
   ```python
   source_directory      = r"C:\caminho\origem"
   destination_directory = r"C:\caminho\destino"
   temp_directory        = r"C:\caminho\temp"
   backup_prefix         = "Backup_Ger_Inteligencia"  # Prefixo do nome do arquivo
   max_backups           = 7                           # Quantidade de backups a manter
   ```

3. Execute:
   ```bash
   python backup.py
   ```

---

## 📁 Estrutura do projeto

```
backup-script/
│
├── backup.py       # Script principal
├── backup.log      # Gerado automaticamente na primeira execução
└── README.md       # Documentação
```

---

## 📋 Fluxo de execução

```
1. Cria diretórios (destino e temporário) se não existirem
2. Compacta o diretório de origem → ZIP no diretório temporário
3. Valida o ZIP (existe? tamanho > 0?)
4. Move o ZIP para o diretório de destino
5. Remove backups antigos (mantém os N mais recentes)
6. Remove o diretório temporário (sempre, com ou sem erro)
```

---

## 📄 Exemplo de log gerado

```
2024-04-15 14:30:22 - INFO - ============================================================
2024-04-15 14:30:22 - INFO - 🚀 Iniciando processo de backup...
2024-04-15 14:30:22 - INFO -    Origem  : C:\dados\origem
2024-04-15 14:30:22 - INFO -    Destino : C:\dados\destino
2024-04-15 14:30:22 - INFO -    Arquivo : Backup_Ger_Inteligencia_20240415_143022.zip
2024-04-15 14:30:25 - INFO - ✅ Compactação concluída (3.12s)
2024-04-15 14:30:25 - INFO - ✅ ZIP validado — tamanho: 245.80 MB
2024-04-15 14:30:26 - INFO - ✅ Arquivo salvo em: C:\dados\destino\Backup_..._20240415_143022.zip (0.95s)
2024-04-15 14:30:26 - INFO - 🗑️  Backup antigo removido: Backup_..._20240401_080000.zip
2024-04-15 14:30:26 - INFO - ✅ Backups antigos verificados — mantendo os 7 mais recentes
2024-04-15 14:30:26 - INFO - ⏱  Tempo total: 0:00:04
2024-04-15 14:30:26 - INFO - ✅ Backup concluído com sucesso!
2024-04-15 14:30:26 - INFO - 🗑️  Diretório temporário removido: C:\dados\temp
2024-04-15 14:30:26 - INFO - ============================================================
```

---

## ⏰ Agendamento automático (Windows)

Para rodar o script automaticamente, use o **Agendador de Tarefas do Windows**:

1. Abra o **Agendador de Tarefas**
2. Clique em **Criar Tarefa Básica**
3. Defina o nome e o gatilho (diário, semanal etc.)
4. Em **Ação**, selecione **Iniciar um programa**
5. Em **Programa/script**, informe o caminho do Python:
   ```
   C:\Users\SEU_USUARIO\AppData\Local\Programs\Python\Python311\python.exe
   ```
6. Em **Adicionar argumentos**, informe o caminho do script:
   ```
   C:\caminho\para\backup.py
   ```

---

## 📌 Observações

- O arquivo `backup.log` é criado automaticamente na mesma pasta do script e acumula o histórico de todas as execuções.
- O diretório temporário é sempre removido ao final, mesmo que ocorra um erro durante o processo.
- Se `max_backups = 7`, o script mantém os 7 ZIPs mais recentes e remove os anteriores automaticamente.
- Caso o diretório de origem não exista ou esteja inacessível, o erro será registrado no log com nível `ERROR`.
