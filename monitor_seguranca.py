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

    def registrar_ataque(self):
        pass

class MonitorDeLogs:
    def __init__(self, caminho_log):
        self.caminho_log = caminho_log

    def vigiar(self):
        print(f"Vigiando o arquivo: {self.caminho_log}")

        
        pass

class GerenciadorFirewall:
    def bloquear_ip(self, ip):
        pass

if __name__ == "__main__":
    print("Iniciando Monitor de Segurança...")

    banco = GerenciadorBD()
    banco.configurar_banco()

    monitor = MonitorDeLogs("/var/log/auth.log")
    monitor.vigiar()