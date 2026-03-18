# 🛡️ Mini Fail2Ban - Monitor de Segurança em Python

Um sistema leve de monitoramento de logs em tempo real desenvolvido em Python. Ele detecta tentativas de intrusão (brute-force) via SSH, extrai o IP do atacante, registra o evento em um banco de dados e simula o bloqueio automático no firewall do Linux.

## 🚀 O Problema que este Projeto Resolve
Servidores expostos à internet sofrem ataques de força bruta constantemente. Este projeto atua como um "cão de guarda" automatizado, lendo logs do sistema em tempo real e fechando as portas para IPs maliciosos antes que eles causem danos, sem a necessidade de intervenção humana.

## ⚙️ Funcionalidades Principais
- **Monitoramento Ao Vivo:** Lê arquivos de log de forma contínua, reagindo instantaneamente a novas entradas.
- **Extração Inteligente (Regex):** Utiliza Expressões Regulares para isolar padrões de endereços IP no meio de textos não estruturados.
- **Persistência de Dados (CRUD):** Armazena o histórico de ataques em um banco de dados relacional SQLite, atualizando status e prevenindo duplicidade de registros.
- **Integração com Sistema Operacional:** Estruturado para acionar regras de bloqueio do `iptables` nativo do Linux via subprocessos.

## 🛠️ Tecnologias Utilizadas
- **Python 3:** Lógica principal e manipulação de arquivos.
- **Expressões Regulares (re):** Para caçar os IPs nos logs.
- **SQLite3:** Banco de dados relacional leve e embutido.
- **Subprocess:** Para comunicação direta com o terminal do sistema operacional.

## 📈 Melhorias Futuras Planejadas

[ ] Implementar envio de alertas por e-mail quando um IP for bloqueado.

[ ] Criar uma interface gráfica simples (Dashboard) para visualizar os ataques.

[ ] Adicionar suporte para ler logs de outros serviços, como Apache ou Nginx.


Desenvolvido por Miguel - Fique à vontade para conectar comigo e enviar feedbacks!