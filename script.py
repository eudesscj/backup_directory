import os
import shutil
import time
import datetime

# 🔹 Configurações
source_directory = r"TROCAR POR DIRETORIO ORIGEM" # Diretório origem
destination_directory = r"TROCAR POR DIRETORIO DESTINO" # Diretório destinatario
temp_directory = r"TROCAR POR DIRETORIO TEMPORARIO"  # Diretório temporário
zip_temp = os.path.join(temp_directory, "TROCAR PELO NOME DO ARQUIVO") # Nome do arquivo
zip_file = zip_temp + ".zip" # Extensão do arquivo

# 🔹 Criar diretórios se não existirem
os.makedirs(destination_directory, exist_ok=True)
os.makedirs(temp_directory, exist_ok=True)

# 🔹 Início do processo
start_time = time.time()

try:
    # 🔹 Compactação no diretório temporário
    step_start = time.time()
    print("🔄 Iniciando compactação...")
    shutil.make_archive(zip_temp, 'zip', source_directory)
    step_end = time.time()
    print(f"✅ Arquivos compactados em {zip_file} ({step_end - step_start:.2f} segundos)")

    # 🔹 Movendo o arquivo ZIP para o destino final
    step_start = time.time()
    final_zip_path = os.path.join(destination_directory, "TROCAR PELO NOME DO ARQUIVO")
    
    # 🔹 Remover ZIP anterior, caso exista
    if os.path.exists(final_zip_path):
        print("🔄 Arquivo ZIP já existe destino. Removendo...")
        os.remove(final_zip_path)
        print("✅ Arquivo ZIP anterior removido.")

    shutil.move(zip_file, final_zip_path)
    step_end = time.time()
    print(f"✅ Arquivo ZIP atualizado em {destination_directory} ({step_end - step_start:.2f} segundos)")

    # 🔹 Removendo o diretório temporário
    shutil.rmtree(temp_directory)
    print(f"✅ Diretório temporário {temp_directory} removido.")

    # 🔹 Fim do processo
    end_time = time.time()
    elapsed_time = end_time - start_time
    formatted_time = str(datetime.timedelta(seconds=int(elapsed_time)))
    print(f"⏱ Tempo total de execução: {formatted_time}")

except Exception as e:
    print(f"❌ Erro ao copiar os arquivos: {e}")
