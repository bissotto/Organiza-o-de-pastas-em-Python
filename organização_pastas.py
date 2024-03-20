import os  # Importa o módulo os para trabalhar com arquivos e diretórios
import shutil  # Importa o módulo shutil para operações de cópia e movimentação de arquivos

# Função para determinar a pasta de destino com base na extensão do arquivo
def get_destination_folder(extension):
    # Dicionário que associa extensões de arquivo a nomes de pastas
    extension_folders = {
        '.txt': 'Textos',
        '.pdf': 'PDFs',
        '.docx': 'Documentos_Word',
        '.jpg': 'Imagens',
        '.png': 'Imagens',
        '.gif': 'Imagens',
        '.mp4': 'Videos',
        '.mp3': 'Audios'
    } 
    # Verifica se a extensão está no dicionário
    if extension in extension_folders:
        # Retorna o nome da pasta associada à extensão
        return extension_folders[extension]
    else:
        # Se a extensão não estiver no dicionário, retorna 'Outros'
        return 'Outros' 
    
# Define o diretório de origem onde os arquivos serão organizados
source_folder = 'C:\\Users\\fabia\\Downloads'

# Loop sobre todos os arquivos no diretório de origem
for file_name in os.listdir(source_folder):
    # Obtém o caminho completo do arquivo
    source_file_path = os.path.join(source_folder, file_name)
    # Verifica se o caminho se refere a um arquivo, não a uma pasta
    if os.path.isfile(source_file_path):
        # Separa o nome do arquivo e sua extensão
        _, extension = os.path.splitext(file_name)
        # Obtém o nome da pasta de destino com base na extensão do arquivo
        destination_folder = get_destination_folder(extension.lower())
        # Obtém ou cria a pasta de destino
        destination_folder_path = os.path.join(source_folder, destination_folder)
        # Verifica se a pasta de destino existe; se não, cria
        if not os.path.exists(destination_folder_path):
            os.makedirs(destination_folder_path)
        # Obtém o caminho completo do novo local do arquivo
        destination_file_path = os.path.join(destination_folder_path, file_name)
        # Move o arquivo para a pasta de destino
        shutil.move(source_file_path, destination_file_path)

# Exibe mensagem após a conclusão da organização
print("Organização concluída!")

