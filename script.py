import os
import shutil
import time
import datetime
import logging
from pathlib import Path

# ──────────────────────────────────────────
# CONFIGURAÇÕES
# ──────────────────────────────────────────
source_directory      = r"TROCAR POR DIRETORIO ORIGEM"       # Diretório a ser compactado
destination_directory = r"TROCAR POR DIRETORIO DESTINO"      # Diretório onde o ZIP será salvo
temp_directory        = r"TROCAR POR DIRETORIO TEMPORARIO"   # Diretório temporário para geração do ZIP
backup_prefix         = "TROCA PELO PREFIXO"                 # Prefixo do nome do arquivo ZIP
max_backups           = 7                                    # Quantidade máxima de backups a manter

# ──────────────────────────────────────────
# CONFIGURAÇÃO DE LOG
# Registra cada execução em backup.log na mesma pasta do script.
# Formato: data/hora - nível - mensagem
# ──────────────────────────────────────────
log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "backup.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_path, encoding="utf-8"),  # Grava no arquivo .log
        logging.StreamHandler()                            # Exibe no console simultaneamente
    ]
)

def limpar_backups_antigos(destination_directory, prefix, max_backups):
    """
    Remove os backups mais antigos mantendo apenas os `max_backups` mais recentes.
    Busca arquivos no destino que correspondam ao padrão: prefix_*.zip
    """
    arquivos = sorted(Path(destination_directory).glob(f"{prefix}_*.zip"))

    if len(arquivos) > max_backups:
        para_remover = arquivos[:-max_backups]  # Todos exceto os N mais recentes
        for arquivo in para_remover:
            arquivo.unlink()
            logging.info(f"🗑️  Backup antigo removido: {arquivo.name}")


def validar_zip(zip_file):
    """
    Verifica se o arquivo ZIP foi gerado corretamente:
    - Deve existir no caminho informado
    - Deve ter tamanho maior que zero bytes
    Lança exceção caso alguma condição não seja atendida.
    """
    if not os.path.exists(zip_file):
        raise Exception(f"Arquivo ZIP não encontrado após compactação: {zip_file}")
    if os.path.getsize(zip_file) == 0:
        raise Exception(f"Arquivo ZIP gerado está vazio: {zip_file}")


def executar_backup():
    """
    Fluxo principal do backup:
      1. Cria os diretórios necessários (destino e temporário)
      2. Compacta o diretório de origem em um ZIP com timestamp
      3. Valida a integridade do ZIP gerado
      4. Move o ZIP para o diretório de destino
      5. Remove backups antigos mantendo apenas os N mais recentes
      6. Garante remoção do diretório temporário mesmo em caso de erro (finally)
    """

    # Timestamp usado no nome do arquivo — formato: YYYYMMDD_HHMMSS
    timestamp    = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_name     = f"{backup_prefix}_{timestamp}"
    zip_temp     = os.path.join(temp_directory, zip_name)   # Caminho temporário sem extensão
    zip_file     = zip_temp + ".zip"                         # Caminho temporário com extensão
    final_zip    = os.path.join(destination_directory, f"{zip_name}.zip")  # Destino final

    # Início da contagem de tempo total
    start_time = time.time()
    logging.info("=" * 60)
    logging.info("🚀 Iniciando processo de backup...")
    logging.info(f"   Origem  : {source_directory}")
    logging.info(f"   Destino : {destination_directory}")
    logging.info(f"   Arquivo : {zip_name}.zip")

    # Cria os diretórios caso não existam
    os.makedirs(destination_directory, exist_ok=True)
    os.makedirs(temp_directory, exist_ok=True)

    try:
        # ── ETAPA 1: Compactação ──────────────────────────────
        step_start = time.time()
        logging.info("🔄 Compactando arquivos...")
        shutil.make_archive(zip_temp, "zip", source_directory)
        logging.info(f"✅ Compactação concluída ({time.time() - step_start:.2f}s)")

        # ── ETAPA 2: Validação do ZIP ─────────────────────────
        validar_zip(zip_file)
        logging.info(f"✅ ZIP validado — tamanho: {os.path.getsize(zip_file) / (1024*1024):.2f} MB")

        # ── ETAPA 3: Mover para o destino final ───────────────
        step_start = time.time()
        logging.info("🔄 Movendo ZIP para o destino...")
        shutil.move(zip_file, final_zip)
        logging.info(f"✅ Arquivo salvo em: {final_zip} ({time.time() - step_start:.2f}s)")

        # ── ETAPA 4: Limpeza de backups antigos ───────────────
        limpar_backups_antigos(destination_directory, backup_prefix, max_backups)
        logging.info(f"✅ Backups antigos verificados — mantendo os {max_backups} mais recentes")

        # Tempo total de execução
        elapsed   = time.time() - start_time
        formatted = str(datetime.timedelta(seconds=int(elapsed)))
        logging.info(f"⏱  Tempo total: {formatted}")
        logging.info("✅ Backup concluído com sucesso!")

    except Exception as e:
        # Registra o erro com nível ERROR para fácil filtragem no log
        logging.error(f"❌ Erro durante o backup: {e}")

    finally:
        # ── ETAPA 5: Limpeza do diretório temporário ──────────
        # Executado sempre — com sucesso ou erro — para não deixar resíduo
        if os.path.exists(temp_directory):
            shutil.rmtree(temp_directory)
            logging.info(f"🗑️  Diretório temporário removido: {temp_directory}")

    logging.info("=" * 60)


# ──────────────────────────────────────────
# EXECUÇÃO
# ──────────────────────────────────────────
if __name__ == "__main__":
    executar_backup()