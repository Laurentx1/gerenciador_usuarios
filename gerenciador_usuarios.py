import subprocess
import os
import sys
import getpass
import re
import ctypes

class UserManager:
    def __init__(self):
        self.request_admin_privileges()
    
    def is_admin(self):
        """Verifica se o script está sendo executado com privilégios de administrador"""
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    
    def request_admin_privileges(self):
        """Solicita privilégios de administrador automaticamente"""
        if not self.is_admin():
            print("🔒 Solicitando privilégios de administrador...")
            print("   Clique 'Sim' na janela do UAC que vai aparecer.")
            
            try:
                # Re-executa o script com privilégios de admin
                ctypes.windll.shell32.ShellExecuteW(
                    None, 
                    "runas", 
                    sys.executable, 
                    " ".join([f'"{arg}"' for arg in sys.argv]), 
                    None, 
                    1
                )
                sys.exit(0)  # Encerra a instância atual
            except Exception as e:
                print(f"❌ Falha ao solicitar privilégios de administrador: {e}")
                print("   Execute manualmente como administrador.")
                input("⏸️  Pressione Enter para continuar mesmo assim...")
        else:
            print("✅ Executando com privilégios de administrador!")
    
    def run_command(self, command, description=""):
        """Executa um comando e trata os resultados"""
        try:
            print(f"🔄 {description}")
            result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding='cp850')
            
            if result.returncode == 0:
                print("✅ Operação realizada com sucesso!")
                if result.stdout.strip():
                    print(f"📋 Output: {result.stdout.strip()}")
                return True
            else:
                print(f"❌ Erro na operação (Código: {result.returncode})")
                if result.stderr.strip():
                    print(f"🔍 Detalhes do erro: {result.stderr.strip()}")
                return False
                
        except Exception as e:
            print(f"💥 Falha ao executar o comando: {e}")
            return False
    
    def validate_username(self, username):
        """Valida o nome de usuário"""
        if not username or len(username.strip()) == 0:
            print("❌ Nome de usuário não pode estar vazio!")
            return False
        
        # Caracteres não permitidos no Windows
        invalid_chars = r'["/\[\]:;|=,+*?<>]'
        if re.search(invalid_chars, username):
            print("❌ Nome de usuário contém caracteres inválidos!")
            return False
        
        if len(username) > 20:
            print("❌ Nome de usuário muito longo (máximo 20 caracteres)!")
            return False
            
        return True
    
    def validate_password(self, password):
        """Valida a senha (critérios básicos)"""
        if len(password) < 6:
            print("❌ Senha deve ter pelo menos 6 caracteres!")
            return False
        return True
    
    def user_exists(self, username):
        """Verifica se o usuário existe"""
        result = subprocess.run(f'net user {username}', shell=True, capture_output=True, text=True)
        return result.returncode == 0
    
    def add_user(self):
        """Cria um novo usuário"""
        print("\n📝 === CRIAR USUÁRIO ===")
        
        username = input("👤 Nome do usuário: ").strip()
        if not self.validate_username(username):
            return
        
        if self.user_exists(username):
            print(f"⚠️  Usuário '{username}' já existe!")
            return
        
        password = getpass.getpass("🔒 Senha (não será exibida): ")
        if not self.validate_password(password):
            return
        
        confirm_password = getpass.getpass("🔒 Confirme a senha: ")
        if password != confirm_password:
            print("❌ Senhas não coincidem!")
            return
        
        full_name = input("📋 Nome completo (opcional): ").strip()
        
        command = f'net user "{username}" "{password}" /add'
        if full_name:
            command += f' /fullname:"{full_name}"'
        
        self.run_command(command, f"Criando usuário '{username}'...")
    
    def delete_user(self):
        """Exclui um usuário"""
        print("\n🗑️  === EXCLUIR USUÁRIO ===")
        
        username = input("👤 Nome do usuário a excluir: ").strip()
        if not self.validate_username(username):
            return
        
        if not self.user_exists(username):
            print(f"❌ Usuário '{username}' não existe!")
            return
        
        # Confirmação de segurança
        confirm = input(f"⚠️  Tem certeza que deseja excluir o usuário '{username}'? (sim/não): ").lower()
        if confirm not in ['sim', 's', 'yes', 'y']:
            print("🚫 Operação cancelada.")
            return
        
        self.run_command(f'net user "{username}" /delete', f"Excluindo usuário '{username}'...")
    
    def add_to_admins(self):
        """Adiciona usuário ao grupo de administradores"""
        print("\n👑 === ADICIONAR AO GRUPO ADMINISTRADORES ===")
        
        username = input("👤 Nome do usuário: ").strip()
        if not self.validate_username(username):
            return
        
        if not self.user_exists(username):
            print(f"❌ Usuário '{username}' não existe!")
            return
        
        # Tenta ambos os nomes do grupo (português e inglês)
        commands = [
            f'net localgroup Administradores "{username}" /add',
            f'net localgroup Administrators "{username}" /add'
        ]
        
        success = False
        for cmd in commands:
            if self.run_command(cmd, f"Adicionando '{username}' aos administradores..."):
                success = True
                break
        
        if not success:
            print("❌ Falha ao adicionar ao grupo de administradores. Verifique o nome do grupo no sistema.")
    
    def remove_from_admins(self):
        """Remove usuário do grupo de administradores"""
        print("\n👤 === REMOVER DO GRUPO ADMINISTRADORES ===")
        
        username = input("👤 Nome do usuário: ").strip()
        if not self.validate_username(username):
            return
        
        if not self.user_exists(username):
            print(f"❌ Usuário '{username}' não existe!")
            return
        
        # Tenta ambos os nomes do grupo
        commands = [
            f'net localgroup Administradores "{username}" /delete',
            f'net localgroup Administrators "{username}" /delete'
        ]
        
        success = False
        for cmd in commands:
            if self.run_command(cmd, f"Removendo '{username}' dos administradores..."):
                success = True
                break
        
        if not success:
            print("❌ Falha ao remover do grupo de administradores.")
    
    def force_password_change(self):
        """Força troca de senha no próximo login"""
        print("\n🔄 === FORÇAR TROCA DE SENHA ===")
        
        username = input("👤 Nome do usuário: ").strip()
        if not self.validate_username(username):
            return
        
        if not self.user_exists(username):
            print(f"❌ Usuário '{username}' não existe!")
            return
        
        self.run_command(
            f'net user "{username}" /logonpasswordchg:yes',
            f"Forçando troca de senha para '{username}'..."
        )
    
    def delete_user_profile(self):
        """Remove pasta do perfil do usuário"""
        print("\n📁 === REMOVER PASTA DO PERFIL ===")
        print("⚠️  ATENÇÃO: Esta operação é IRREVERSÍVEL!")
        print("   Todos os dados do perfil serão perdidos permanentemente.")
        
        username = input("👤 Nome do usuário: ").strip()
        if not self.validate_username(username):
            return
        
        profile_path = f"C:\\Users\\{username}"
        
        if not os.path.exists(profile_path):
            print(f"❌ Pasta do perfil não encontrada: {profile_path}")
            return
        
        # Dupla confirmação para operação perigosa
        print(f"📂 Pasta encontrada: {profile_path}")
        confirm1 = input("⚠️  Digite 'CONFIRMAR' para prosseguir: ").upper()
        if confirm1 != "CONFIRMAR":
            print("🚫 Operação cancelada.")
            return
        
        confirm2 = input("⚠️  Tem absoluta certeza? Digite 'SIM' para confirmar: ").upper()
        if confirm2 != "SIM":
            print("🚫 Operação cancelada.")
            return
        
        self.run_command(
            f'rmdir /s /q "{profile_path}"',
            f"Removendo pasta do perfil de '{username}'..."
        )
    
    def list_users(self):
        """Lista todos os usuários do sistema"""
        print("\n📋 === USUÁRIOS DO SISTEMA ===")
        self.run_command('net user', "Listando usuários do sistema...")
    
    def show_user_info(self):
        """Mostra informações detalhadas de um usuário"""
        print("\n📊 === INFORMAÇÕES DO USUÁRIO ===")
        
        username = input("👤 Nome do usuário: ").strip()
        if not self.validate_username(username):
            return
        
        self.run_command(f'net user "{username}"', f"Obtendo informações de '{username}'...")
    
    def menu(self):
        """Menu principal do programa"""
        while True:
            print("\n" + "="*50)
            print("🐍 GERENCIADOR DE USUÁRIOS WINDOWS")
            print("="*50)
            print("[1] 👤 Criar usuário")
            print("[2] 🗑️  Excluir usuário")
            print("[3] 👑 Adicionar ao grupo de administradores")
            print("[4] 👤 Remover do grupo de administradores")
            print("[5] 🔄 Forçar troca de senha no próximo login")
            print("[6] 📁 Apagar pasta do perfil do usuário")
            print("[7] 📋 Listar usuários do sistema")
            print("[8] 📊 Mostrar informações de usuário")
            print("[0] 🚪 Sair")
            print("-" * 50)
            
            try:
                opcao = input("🎯 Escolha uma opção: ").strip()
                
                if opcao == "1":
                    self.add_user()
                elif opcao == "2":
                    self.delete_user()
                elif opcao == "3":
                    self.add_to_admins()
                elif opcao == "4":
                    self.remove_from_admins()
                elif opcao == "5":
                    self.force_password_change()
                elif opcao == "6":
                    self.delete_user_profile()
                elif opcao == "7":
                    self.list_users()
                elif opcao == "8":
                    self.show_user_info()
                elif opcao == "0":
                    print("👋 Encerrando o gerenciador...")
                    break
                else:
                    print("❌ Opção inválida! Tente novamente.")
                    
                input("\n⏸️  Pressione Enter para continuar...")
                
            except KeyboardInterrupt:
                print("\n\n🛑 Programa interrompido pelo usuário.")
                break
            except Exception as e:
                print(f"💥 Erro inesperado: {e}")
                input("⏸️  Pressione Enter para continuar...")

def main():
    """Função principal"""
    print("🚀 Iniciando Gerenciador de Usuários Windows...")
    
    # Verifica se está no Windows
    if os.name != 'nt':
        print("❌ Este script foi desenvolvido para Windows.")
        return
    
    try:
        manager = UserManager()
        manager.menu()
    except Exception as e:
        print(f"💥 Erro fatal: {e}")
        input("⏸️  Pressione Enter para sair...")

if __name__ == "__main__":
    main()