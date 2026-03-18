import sqlite3
import time
import subprocess
import re
from ctypes.wintypes import HMONITOR


class GerenciadorBD:
    def __init__(self):
        self.conexao = sqlite3.connect('seguranca.db')
        self.cursor = self.conexao.cursor()

    def configurar_banco(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS ataques (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ip TEXT UNIQUE NOT NULL,
                tentativas INTEGER Default 1,
                ultima_tentativa TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                status TEXT DEFAULT 'monitorando'
                )
        ''')
        self.conexao.commit()
        pass

    def registrar_ataque(self, ip):
        def atualizar_status(self, ip, novo_status):
            self.cursor.execute('''
                                UPDATE ataques
                                SET status = ?
                                WHERE ip = ?
                                ''', (novo_status, ip))

            self.conexao.commit()
            print(f"✅ Status do IP {ip} atualizado para: '{novo_status}' no banco de dados!")

        self.cursor.execute('''
                            INSERT INTO ataques (ip, tentativas)
                            VALUES (?, 1) ON CONFLICT(ip) DO
                            UPDATE SET
                                tentativas = tentativas + 1,
                                ultima_tentativa = CURRENT_TIMESTAMP
                            ''', (ip,))

        self.conexao.commit()
        print(f"💾 Registro salvo no banco: IP {ip} atacou o sistema!")


class MonitorDeLogs:
    def __init__(self, caminho_log, banco, firewall):
        self.caminho_log = caminho_log
        self.banco = banco
        self.firewall = firewall

    def vigiar(self):
        print(f"Vigiando o arquivo: {self.caminho_log}")

        with open(self.caminho_log, 'r', encoding='utf-8') as arquivo:

            #arquivo.seek(0, 2)

            while True:
                linha = arquivo.readline()

                if linha:
                    if "Failed password" in linha:

                        busca_ip = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', linha)

                        if busca_ip:

                            ip_atacante = busca_ip.group()
                            print(f"🚨 ALERTA DE INVASÃO! IP isolado: {ip_atacante}")
                            self.banco.registrar_ataque(ip_atacante)
                            self.firewall.bloquear_ip(ip_atacante)
                            self.banco.atualizar_status(ip_atacante, 'bloqueado')
                        else:
                            print("🚨 ALERTA DE INVASÃO! (Mas nenhum IP foi encontrado na linha)")

                else:
                    time.sleep(0.1)

                    pass


class GerenciadorFirewall:
    def bloquear_ip(self, ip):
        print(f" Acionando o Firewall contra o IP: {ip}...")

        comando_linux = ["iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"]

        try:

            # subprocess.run(comando_linux, check=True)
            print(f"🚫 [SIMULAÇÃO LINUX] Regra aplicada: {' '.join(comando_linux)}")
        except Exception as e:
            print(f"⚠️ Erro ao tentar bloquear no firewall: {e}")

if __name__ == "__main__":
    print("Iniciando Monitor de Segurança...")

    banco = GerenciadorBD()
    banco.configurar_banco()

    firewall = GerenciadorFirewall()


    monitor = MonitorDeLogs(r"C:\Users\migue\PycharmProjects\MiniFail2BAN\teste_log.txt", banco, firewall)
    monitor.vigiar()