# Gerenciador de Usuários Windows

## Visão Geral

Uma ferramenta abrangente baseada em Python para gerenciamento de contas de usuário Windows com privilégios administrativos. Esta aplicação fornece uma interface amigável via linha de comando para executar tarefas comuns de gerenciamento de usuários em sistemas Windows, incluindo criação, exclusão, gerenciamento de privilégios e manutenção de perfis.

## Funcionalidades

- **Gerenciamento de Contas de Usuário**
  - Criar novas contas de usuário com validação de senha
  - Excluir contas de usuário existentes com confirmações de segurança
  - Listar todos os usuários do sistema
  - Exibir informações detalhadas do usuário

- **Privilégios Administrativos**
  - Adicionar usuários ao grupo Administradores
  - Remover usuários do grupo Administradores
  - Solicitação automática de elevação de privilégios

- **Gerenciamento de Senhas**
  - Entrada segura de senha (oculta da visualização)
  - Validação de força da senha
  - Forçar alteração de senha no próximo login

- **Gerenciamento de Perfis**
  - Exclusão completa do perfil do usuário
  - Remoção segura de diretórios de usuário

- **Recursos de Segurança**
  - Validação e sanitização de entrada
  - Prompts de confirmação para operações destrutivas
  - Verificação de privilégios de administrador

## Requisitos

- Sistema operacional Windows
- Python 3.6 ou superior
- Privilégios de administrador (solicitados automaticamente)

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/Laurentx1/gerenciador-usuarios.git
cd gerenciador-usuarios
```

2. Execute o script:
```bash
python gerenciador-usuarios.py
```

A aplicação solicitará automaticamente privilégios de administrador se não estiver executando com permissões elevadas.

## Uso

Inicie a aplicação e selecione uma das seguintes opções:

1. **Criar Usuário** - Adicionar uma nova conta de usuário ao sistema
2. **Excluir Usuário** - Remover uma conta de usuário existente
3. **Adicionar aos Administradores** - Conceder privilégios administrativos a um usuário
4. **Remover dos Administradores** - Revogar privilégios administrativos de um usuário
5. **Forçar Troca de Senha** - Exigir alteração de senha no próximo login
6. **Excluir Perfil do Usuário** - Remover diretório e dados do perfil do usuário
7. **Listar Usuários** - Exibir todos os usuários do sistema
8. **Mostrar Informações do Usuário** - Visualizar informações detalhadas sobre um usuário específico

## Validação de Entrada

A aplicação inclui validação abrangente de entrada:

- Restrições de comprimento do nome de usuário (máximo 20 caracteres)
- Detecção de caracteres inválidos para nomes de usuário Windows
- Requisitos de força da senha (mínimo 6 caracteres)
- Prompts de confirmação para operações destrutivas

## Tratamento de Erros

- Tratamento elegante de falhas na execução de comandos
- Mensagens de erro detalhadas com informações de solução de problemas
- Cancelamento seguro de operações para proteção do usuário

## Considerações de Segurança

Esta ferramenta requer privilégios de administrador para funcionar adequadamente. Sempre certifique-se de:

- Executar a aplicação apenas em sistemas confiáveis
- Verificar credenciais de usuário antes de fazer alterações
- Usar senhas fortes para novas contas
- Revisar alterações antes de confirmar operações destrutivas

## Compatibilidade de Plataforma

- **Suportado**: Windows 10, Windows 11, Windows Server 2016+
- **Suporte a Idiomas**: Instalações Windows em português e inglês
- **Arquitetura**: Compatível com sistemas 32-bit e 64-bit

## Implementação Técnica

- Construído com módulos da biblioteca padrão Python
- Utiliza comandos Windows `net user` e `net localgroup`
- Implementa integração com UAC (Controle de Conta de Usuário) do Windows
- Tratamento de codificação de caracteres para prompt de comando Windows

## Estrutura do Código

```
gerenciador-usuarios.py
├── Classe UserManager
│   ├── Verificação de privilégios administrativos
│   ├── Execução de comandos do sistema
│   ├── Validação de entrada
│   ├── Gerenciamento de usuários
│   └── Interface do menu principal
└── Função principal e inicialização
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para enviar um Pull Request. Para mudanças importantes, por favor abra uma issue primeiro para discutir o que você gostaria de alterar.

### Como Contribuir

1. Faça um fork do projeto
2. Crie uma branch para sua feature (git checkout -b feature/NovaFuncionalidade)
3. Commit suas mudanças (git commit -m 'Adiciona nova funcionalidade')
4. Push para a branch (git push origin feature/NovaFuncionalidade)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.

## Aviso Legal

Esta ferramenta modifica contas de usuário do sistema e deve ser usada com cautela. Sempre teste em um ambiente controlado antes de usar em sistemas de produção. Os autores não são responsáveis por quaisquer modificações do sistema ou perda de dados resultantes do uso desta ferramenta.

## Suporte

Para problemas, solicitações de recursos ou dúvidas, por favor abra uma issue no GitHub ou entre em contato com os mantenedores.

## Changelog

### Versão 1.0.0
- Implementação inicial do gerenciador de usuários
- Interface de linha de comando interativa
- Validação completa de entrada
- Suporte para sistemas Windows em português e inglês
- Integração com UAC para elevação automática de privilégios
