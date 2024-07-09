# -*- coding: utf-8 -*-
"""bitcoin puzzle.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lqxKGQ1W6XhMYNLXYLfN4_Lc3D2RPBqy
"""

import requests

def get_btc_balance(address):
    url = f'https://blockchain.info/rawaddr/{address}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        balance = data['final_balance'] / 1e8  # Converter satoshis para BTC
        return balance
    else:
        return None

address = '13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so'
balance = get_btc_balance(address)

if balance is not None:
    print(f'Saldo de {address}: {balance} BTC')
else:
    print('Erro ao obter o saldo da carteira.')

!sudo apt-get update
!sudo apt-get install -y libgmp-dev libmpc-dev libmpfr-dev
!pip install fastecdsa

pip install bitcoinlib

pip install ecdsa base58

from bitcoinlib.keys import Key

# Chave privada fornecida
private_key = '0000000000000000000000000000000000000000000000000000000000000001'

# Criar uma chave a partir da chave privada
key = Key(private_key)

# Obter o endereço da carteira a partir da chave
address = key.address()

# Verificar se o endereço corresponde ao endereço fornecido
expected_address = '1BgGZ9tcN4rm9KBzDn7KprQz87SZ26SAMH'
print(f"Endereço da carteira: {address}")
print(f"Endereço corresponde: {address == expected_address}")

!pip install pycryptodome

import hashlib
from binascii import unhexlify, hexlify
import threading
from tqdm import tqdm
from bitcoinlib.keys import Key

def private_key_to_public_key(private_key):
    # Converte a chave privada para uma chave pública usando bitcoinlib
    key = Key(private_key)
    public_key = key.public_hex
    return public_key

def public_key_to_address(public_key):
    # Converte a chave pública para um endereço Bitcoin manualmente
    key = Key(import_key=public_key)
    address = key.address()
    return address

def check_address(public_key, target_address):
    # Verifica se a chave pública corresponde ao endereço de destino
    address = public_key_to_address(public_key)
    return address == target_address

def try_keys(start, end, target_address, thread_id, progress_bar, itera_por_tred):
    global found
    attempts = 0
    private_key_int = start
    while not found and private_key_int <= end:
        private_key = hexlify(private_key_int.to_bytes(32, byteorder='big')).decode('utf-8')
        public_key = private_key_to_public_key(private_key)
        if check_address(public_key, target_address):
            found = True
            print(f'\n[Thread {thread_id}] Chave encontrada após {attempts} tentativas!')
            print(f'Chave privada: {private_key}')
            print(f'Chave pública: {public_key}\n')
            break
        private_key_int += 1
        attempts += 1
        progress_bar.update(1)
        if attempts % itera_por_tred == 0:
            break

    if not found:
        print(f'\n[Thread {thread_id}] Chave não encontrada no intervalo fornecido.')
        print(f'Última chave privada tentada: {private_key}\n')

target_address = '1McVt1vMtCC7yn5b9wgX1833yCcLXzueeC'
start = int('1', 16)
end = int('ff', 16)

num_threads = 1  # Iniciando com 1 thread
itera_por_tred = 100
found = False

# Calcula o número total de possibilidades
num_possibilities = end - start + 1

# Cria uma barra de progresso
progress_bar = tqdm(total=num_possibilities, desc="Progresso total")

# Divide o intervalo entre as threads
thread_range = (end - start + 1) // num_threads
threads = []

for i in range(num_threads):
    thread_start = start + i * thread_range
    thread_end = thread_start + thread_range - 1 if i < num_threads - 1 else end
    thread = threading.Thread(target=try_keys, args=(thread_start, thread_end, target_address, i + 1, progress_bar, itera_por_tred))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

progress_bar.close()

if not found:
    print('\nChave não encontrada no intervalo fornecido.')

import hashlib
from binascii import unhexlify, hexlify
import threading
from tqdm import tqdm
from bitcoinlib.keys import Key
import time
import requests
import random

# Substitua pelo seu token de bot
bot_token = '7416147739:AAF9wVvdjE6JqRrPY2i7POGMyjzHqEtBMQU'

# Dados das carteiras (wallet_data) - assumimos que já estão definidos

# Função para obter dados do objeto pelo ID
def get_wallet_data(wallet_id):
    if wallet_id in wallet_data:
        return wallet_data[wallet_id]
    else:
        print(f'Wallet ID {wallet_id} não encontrado.')
        return None

# Função para obter atualizações e extrair o chat_id
def get_chat_id(bot_token):
    url = f'https://api.telegram.org/bot{bot_token}/getUpdates'
    response = requests.get(url)

    if response.status_code == 200:
        updates = response.json()
        if updates['result']:
            # Obtém o primeiro chat_id disponível nas atualizações
            chat_id = updates['result'][0]['message']['chat']['id']
            return chat_id
        else:
            print('Nenhuma atualização encontrada.')
            return None
    else:
        print(f'Falha ao obter atualizações. Status code: {response.status_code}')
        print('Detalhes:', response.json())
        return None

def private_key_to_public_key(private_key):
    # Converte a chave privada para uma chave pública usando bitcoinlib
    key = Key(private_key)
    public_key = key.public_hex
    return public_key

def public_key_to_address(public_key):
    # Converte a chave pública para um endereço Bitcoin manualmente
    key = Key(import_key=public_key)
    address = key.address()
    return address

def check_address(public_key, target_address):
    # Verifica se a chave pública corresponde ao endereço de destino
    address = public_key_to_address(public_key)
    return address == target_address

def try_keys(start, end, target_address, thread_id, progress_bar, itera_por_tred):
    global found
    attempts = 0
    private_key_int = start

    while not found and private_key_int <= end:
        private_key_int = random.randint(start, end)
        private_key = hexlify(private_key_int.to_bytes(32, byteorder='big')).decode('utf-8')
        public_key = private_key_to_public_key(private_key)

        if check_address(public_key, target_address):
            found = True
            print(f'\n[Wallet_id: {wallet_id}] Chave encontrada após {attempts} tentativas!')
            print(f'Chave privada: {private_key}')
            print(f'Chave pública: {public_key}\n')
            chat_id = get_chat_id(bot_token)
            if chat_id:
                # Mensagem com variáveis dinâmicas
                message = f'\n\n🔍 [ID da Wallet: {wallet_id}]\n\n ✅✅✅ \n\n Chave encontrada!! \n\n {attempts} tentativas!\n\n ✅✅✅ \n\n 🔑 Chave privada: \n\n[{private_key}]\n\n 🔑 Chave pública: \n\n[{public_key}]\n'

                # URL da API do Telegram para envio de mensagens
                url = f'https://api.telegram.org/bot{bot_token}/sendMessage'

                # Parâmetros da requisição
                params = {
                    'chat_id': chat_id,
                    'text': message
                }

                # Enviando a requisição
                response = requests.get(url, params=params)

                # Verificando a resposta
                if response.status_code == 200:
                    print('Mensagem enviada com sucesso!')
                else:
                    print(f'Falha ao enviar mensagem. Status code: {response.status_code}')
                    print('Detalhes:', response.json())
            else:
                print('Não foi possível obter o chat_id.')
            break

        attempts += 1
        progress_bar.update(1)
        if attempts == itera_por_tred:
            break

    if not found:
        print(f'\n[Thread {thread_id}] Chave não encontrada no intervalo fornecido.')
        print(f'Última chave privada tentada: {private_key}\n')
        chat_id = get_chat_id(bot_token)

        if chat_id:

            message = f'\n  🔍  [ID da Wallet: {wallet_id}]\n\n❌❌❌\n\n Chave não encontrada no intervalo fornecido!  \n\n ❌❌❌\n\n 🔑   Última chave privada tentada:\n\n [{private_key}]'
            # URL da API do Telegram para envio de mensagens
            url = f'https://api.telegram.org/bot{bot_token}/sendMessage'

            # Parâmetros da requisição
            params = {
                'chat_id': chat_id,
                'text': message
            }
            url = f'https://api.telegram.org/bot{bot_token}/sendMessage'

            # Parâmetros da requisição
            params = {
                'chat_id': chat_id,
                'text': message,
            }

            # Enviando a requisição
            response = requests.get(url, params=params)

            # Verificando a resposta
            if response.status_code == 200:
                print('\nMensagem enviada com sucesso!')
            else:
                print(f'Falha ao enviar mensagem. Status code: {response.status_code}')
                print('Detalhes:', response.json())
        else:
            print('Não foi possível obter o chat_id.')

# ID da wallet a ser usada
wallet_id = '66'  # Altere este valor conforme necessário

# Obtenha os dados da wallet usando o ID
wallet_info = get_wallet_data(wallet_id)

if wallet_info:
    target_address = wallet_info['WALLET']
    start = int(wallet_info['START'], 16)
    end = int(wallet_info['END'], 16)

    num_threads = 1  # Iniciando com 1 thread
    itera_por_tred = 1999999
    found = False

    # Calcula o número total de possibilidades
    num_possibilities = end - start + 1

    # Cria uma barra de progresso
    progress_bar = tqdm(total=itera_por_tred, desc="Progresso total")

    # Medir o tempo de execução
    start_time = time.time()

    # Divide o intervalo entre as threads
    thread_range = (end - start + 1) // num_threads
    threads = []

    for i in range(num_threads):
        thread_start = start + i * thread_range
        thread_end = thread_start + thread_range - 1 if i < num_threads - 1 else end
        thread = threading.Thread(target=try_keys, args=(thread_start, thread_end, target_address, i + 1, progress_bar, itera_por_tred))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    progress_bar.close()

    end_time = time.time()
    execution_time = end_time - start_time

    print(f'Tempo de execução: {execution_time} segundos')

    if not found:
        print('\nChave não encontrada no intervalo fornecido.')
else:
    print('Dados da wallet não encontrados.')

wallet_data = {
    "1": {
        "WALLET": "1BgGZ9tcN4rm9KBzDn7KprQz87SZ26SAMH",
        "START": "0x1",
        "END": "0x1"
    },
    "2": {
        "WALLET": "1CUNEBjYrCn2y1SdiUMohaKUi4wpP326Lb",
        "START": "0x2",
        "END": "0x3"
    },
    "3": {
        "WALLET": "19ZewH8Kk1PDbSNdJ97FP4EiCjTRaZMZQA",
        "START": "0x4",
        "END": "0x7"
    },
    "4": {
        "WALLET": "1EhqbyUMvvs7BfL8goY6qcPbD6YKfPqb7e",
        "START": "0x8",
        "END": "0xf"
    },
    "5": {
        "WALLET": "1E6NuFjCi27W5zoXg8TRdcSRq84zJeBW3k",
        "START": "0x10",
        "END": "0x1f"
    },
    "6": {
        "WALLET": "1PitScNLyp2HCygzadCh7FveTnfmpPbfp8",
        "START": "0x20",
        "END": "0x3f"
    },
    "7": {
        "WALLET": "1McVt1vMtCC7yn5b9wgX1833yCcLXzueeC",
        "START": "0x40",
        "END": "0x7f"
    },
    "8": {
        "WALLET": "1M92tSqNmQLYw33fuBvjmeadirh1ysMBxK",
        "START": "0x80",
        "END": "0xff"
    },
    "9": {
        "WALLET": "1CQFwcjw1dwhtkVWBttNLDtqL7ivBonGPV",
        "START": "0x100",
        "END": "0x1ff"
    },
    "10": {
        "WALLET": "1LeBZP5QCwwgXRtmVUvTVrraqPUokyLHqe",
        "START": "0x200",
        "END": "0x3ff"
    },
    "11": {
        "WALLET": "1PgQVLmst3Z314JrQn5TNiys8Hc38TcXJu",
        "START": "0x400",
        "END": "0x7ff"
    },
    "12": {
        "WALLET": "1DBaumZxUkM4qMQRt2LVWyFJq5kDtSZQot",
        "START": "0x800",
        "END": "0xfff"
    },
    "13": {
        "WALLET": "1Pie8JkxBT6MGPz9Nvi3fsPkr2D8q3GBc1",
        "START": "0x1000",
        "END": "0x1fff"
    },
    "14": {
        "WALLET": "1ErZWg5cFCe4Vw5BzgfzB74VNLaXEiEkhk",
        "START": "0x2000",
        "END": "0x3fff"
    },
    "15": {
        "WALLET": "1QCbW9HWnwQWiQqVo5exhAnmfqKRrCRsvW",
        "START": "0x4000",
        "END": "0x7fff"
    },
    "16": {
        "WALLET": "1BDyrQ6WoF8VN3g9SAS1iKZcPzFfnDVieY",
        "START": "0x8000",
        "END": "0xffff"
    },
    "17": {
        "WALLET": "1HduPEXZRdG26SUT5Yk83mLkPyjnZuJ7Bm",
        "START": "0x10000",
        "END": "0x1ffff"
    },
    "18": {
        "WALLET": "1GnNTmTVLZiqQfLbAdp9DVdicEnB5GoERE",
        "START": "0x20000",
        "END": "0x3ffff"
    },
    "19": {
        "WALLET": "1NWmZRpHH4XSPwsW6dsS3nrNWfL1yrJj4w",
        "START": "0x40000",
        "END": "0x7ffff"
    },
    "20": {
        "WALLET": "1HsMJxNiV7TLxmoF6uJNkydxPFDog4NQum",
        "START": "0x80000",
        "END": "0xfffff"
    },
    "21": {
        "WALLET": "14oFNXucftsHiUMY8uctg6N487riuyXs4h",
        "START": "0x100000",
        "END": "0x1fffff"
    },
    "22": {
        "WALLET": "1CfZWK1QTQE3eS9qn61dQjV89KDjZzfNcv",
        "START": "0x200000",
        "END": "0x3fffff"
    },
    "23": {
        "WALLET": "1L2GM8eE7mJWLdo3HZS6su1832NX2txaac",
        "START": "0x400000",
        "END": "0x7fffff"
    },
    "24": {
        "WALLET": "1rSnXMr63jdCuegJFuidJqWxUPV7AtUf7",
        "START": "0x800000",
        "END": "0xffffff"
    },
    "25": {
        "WALLET": "15JhYXn6Mx3oF4Y7PcTAv2wVVAuCFFQNiP",
        "START": "0x1000000",
        "END": "0x1ffffff"
    },
    "26": {
        "WALLET": "1JVnST957hGztonaWK6FougdtjxzHzRMMg",
        "START": "0x2000000",
        "END": "0x3ffffff"
    },
    "27": {
        "WALLET": "128z5d7nN7PkCuX5qoA4Ys6pmxUYnEy86k",
        "START": "0x4000000",
        "END": "0x7ffffff"
    },
    "28": {
        "WALLET": "12jbtzBb54r97TCwW3G1gCFoumpckRAPdY",
        "START": "0x8000000",
        "END": "0xfffffff"
    },
    "29": {
        "WALLET": "19EEC52krRUK1RkUAEZmQdjTyHT7Gp1TYT",
        "START": "0x10000000",
        "END": "0x1fffffff"
    },
    "30": {
        "WALLET": "1LHtnpd8nU5VHEMkG2TMYYNUjjLc992bps",
        "START": "0x20000000",
        "END": "0x3fffffff"
    },
    "31": {
        "WALLET": "1LhE6sCTuGae42Axu1L1ZB7L96yi9irEBE",
        "START": "0x40000000",
        "END": "0x7fffffff"
    },
    "32": {
        "WALLET": "1FRoHA9xewq7DjrZ1psWJVeTer8gHRqEvR",
        "START": "0x80000000",
        "END": "0xffffffff"
    },
    "33": {
        "WALLET": "187swFMjz1G54ycVU56B7jZFHFTNVQFDiu",
        "START": "0x100000000",
        "END": "0x1ffffffff"
    },
    "34": {
        "WALLET": "1PWABE7oUahG2AFFQhhvViQovnCr4rEv7Q",
        "START": "0x200000000",
        "END": "0x3ffffffff"
    },
    "35": {
        "WALLET": "1PWCx5fovoEaoBowAvF5k91m2Xat9bMgwb",
        "START": "0x400000000",
        "END": "0x7ffffffff"
    },
    "36": {
        "WALLET": "1Be2UF9NLfyLFbtm3TCbmuocc9N1Kduci1",
        "START": "0x800000000",
        "END": "0xfffffffff"
    },
    "37": {
        "WALLET": "14iXhn8bGajVWegZHJ18vJLHhntcpL4dex",
        "START": "0x1000000000",
        "END": "0x1fffffffff"
    },
    "38": {
        "WALLET": "1HBtApAFA9B2YZw3G2YKSMCtb3dVnjuNe2",
        "START": "0x2000000000",
        "END": "0x3fffffffff"
    },
    "39": {
        "WALLET": "122AJhKLEfkFBaGAd84pLp1kfE7xK3GdT8",
        "START": "0x4000000000",
        "END": "0x7fffffffff"
    },
    "40": {
        "WALLET": "1EeAxcprB2PpCnr34VfZdFrkUWuxyiNEFv",
        "START": "0x8000000000",
        "END": "0xffffffffff"
    },
    "41": {
        "WALLET": "1L5sU9qvJeuwQUdt4y1eiLmquFxKjtHr3E",
        "START": "0x10000000000",
        "END": "0x1ffffffffff"
    },
    "42": {
        "WALLET": "1E32GPWgDyeyQac4aJxm9HVoLrrEYPnM4N",
        "START": "0x20000000000",
        "END": "0x3ffffffffff"
    },
    "43": {
        "WALLET": "1PiFuqGpG8yGM5v6rNHWS3TjsG6awgEGA1",
        "START": "0x40000000000",
        "END": "0x7ffffffffff"
    },
    "44": {
        "WALLET": "1CkR2uS7LmFwc3T2jV8C1BhWb5mQaoxedF",
        "START": "0x80000000000",
        "END": "0xfffffffffff"
    },
    "45": {
        "WALLET": "1NtiLNGegHWE3Mp9g2JPkgx6wUg4TW7bbk",
        "START": "0x100000000000",
        "END": "0x1fffffffffff"
    },
    "46": {
        "WALLET": "1F3JRMWudBaj48EhwcHDdpeuy2jwACNxjP",
        "START": "0x200000000000",
        "END": "0x3fffffffffff"
    },
    "47": {
        "WALLET": "1Pd8VvT49sHKsmqrQiP61RsVwmXCZ6ay7Z",
        "START": "0x400000000000",
        "END": "0x7fffffffffff"
    },
    "48": {
        "WALLET": "1DFYhaB2J9q1LLZJWKTnscPWos9VBqDHzv",
        "START": "0x800000000000",
        "END": "0xffffffffffff"
    },
    "49": {
        "WALLET": "12CiUhYVTTH33w3SPUBqcpMoqnApAV4WCF",
        "START": "0x1000000000000",
        "END": "0x1ffffffffffff"
    },
    "50": {
        "WALLET": "1MEzite4ReNuWaL5Ds17ePKt2dCxWEofwk",
        "START": "0x2000000000000",
        "END": "0x3ffffffffffff"
    },
    "51": {
        "WALLET": "1NpnQyZ7x24ud82b7WiRNvPm6N8bqGQnaS",
        "START": "0x4000000000000",
        "END": "0x7ffffffffffff"
    },
    "52": {
        "WALLET": "15z9c9sVpu6fwNiK7dMAFgMYSK4GqsGZim",
        "START": "0x8000000000000",
        "END": "0xfffffffffffff"
    },
    "53": {
        "WALLET": "15K1YKJMiJ4fpesTVUcByoz334rHmknxmT",
        "START": "0x10000000000000",
        "END": "0x1fffffffffffff"
    },
    "54": {
        "WALLET": "1KYUv7nSvXx4642TKeuC2SNdTk326uUpFy",
        "START": "0x20000000000000",
        "END": "0x3fffffffffffff"
    },
    "55": {
        "WALLET": "1LzhS3k3e9Ub8i2W1V8xQFdB8n2MYCHPCa",
        "START": "0x40000000000000",
        "END": "0x7fffffffffffff"
    },
    "56": {
        "WALLET": "17aPYR1m6pVAacXg1PTDDU7XafvK1dxvhi",
        "START": "0x80000000000000",
        "END": "0xffffffffffffff"
    },
    "57": {
        "WALLET": "15c9mPGLku1HuW9LRtBf4jcHVpBUt8txKz",
        "START": "0x100000000000000",
        "END": "0x1ffffffffffffff"
    },
    "58": {
        "WALLET": "1Dn8NF8qDyyfHMktmuoQLGyjWmZXgvosXf",
        "START": "0x200000000000000",
        "END": "0x3ffffffffffffff"
    },
    "59": {
        "WALLET": "1HAX2n9Uruu9YDt4cqRgYcvtGvZj1rbUyt",
        "START": "0x400000000000000",
        "END": "0x7ffffffffffffff"
    },
    "60": {
        "WALLET": "1Kn5h2qpgw9mWE5jKpk8PP4qvvJ1QVy8su",
        "START": "0x800000000000000",
        "END": "0xfffffffffffffff"
    },
    "61": {
        "WALLET": "1AVJKwzs9AskraJLGHAZPiaZcrpDr1U6AB",
        "START": "0x1000000000000000",
        "END": "0x1fffffffffffffff"
    },
    "62": {
        "WALLET": "1Me6EfpwZK5kQziBwBfvLiHjaPGxCKLoJi",
        "START": "0x2000000000000000",
        "END": "0x3fffffffffffffff"
    },
    "63": {
        "WALLET": "1NpYjtLira16LfGbGwZJ5JbDPh3ai9bjf4",
        "START": "0x4000000000000000",
        "END": "0x7fffffffffffffff"
    },
    "64": {
        "WALLET": "16jY7qLJnxb7CHZyqBP8qca9d51gAjyXQN",
        "START": "0x8000000000000000",
        "END": "0xffffffffffffffff"
    },
    "65": {
        "WALLET": "18ZMbwUFLMHoZBbfpCjUJQTCMCbktshgpe",
        "START": "0x10000000000000000",
        "END": "0x1ffffffffffffffff"
    },
    "66": {
        "WALLET": "13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so",
        "START": "0x20000000000000000",
        "END": "0x3ffffffffffffffff"
    },
    "67": {
        "WALLET": "1BY8GQbnueYofwSuFAT3USAhGjPrkxDdW9",
        "START": "0x40000000000000000",
        "END": "0x7ffffffffffffffff"
    },
    "68": {
        "WALLET": "1MVDYgVaSN6iKKEsbzRUAYFrYJadLYZvvZ",
        "START": "0x80000000000000000",
        "END": "0xfffffffffffffffff"
    },
    "69": {
        "WALLET": "19vkiEajfhuZ8bs8Zu2jgmC6oqZbWqhxhG",
        "START": "0x100000000000000000",
        "END": "0x1fffffffffffffffff"
    },
    "70": {
        "WALLET": "19YZECXj3SxEZMoUeJ1yiPsw8xANe7M7QR",
        "START": "0x200000000000000000",
        "END": "0x3fffffffffffffffff"
    },
    "71": {
        "WALLET": "1PWo3JeB9jrGwfHDNpdGK54CRas7fsVzXU",
        "START": "0x400000000000000000",
        "END": "0x7fffffffffffffffff"
    },
    "72": {
        "WALLET": "1JTK7s9YVYywfm5XUH7RNhHJH1LshCaRFR",
        "START": "0x800000000000000000",
        "END": "0xffffffffffffffffff"
    },
    "73": {
        "WALLET": "12VVRNPi4SJqUTsp6FmqDqY5sGosDtysn4",
        "START": "0x1000000000000000000",
        "END": "0x1ffffffffffffffffff"
    },
    "74": {
        "WALLET": "1FWGcVDK3JGzCC3WtkYetULPszMaK2Jksv",
        "START": "0x2000000000000000000",
        "END": "0x3ffffffffffffffffff"
    },
    "75": {
        "WALLET": "1J36UjUByGroXcCvmj13U6uwaVv9caEeAt",
        "START": "0x4000000000000000000",
        "END": "0x7ffffffffffffffffff"
    },
    "76": {
        "WALLET": "1DJh2eHFYQfACPmrvpyWc8MSTYKh7w9eRF",
        "START": "0x8000000000000000000",
        "END": "0xfffffffffffffffffff"
    },
    "77": {
        "WALLET": "1Bxk4CQdqL9p22JEtDfdXMsng1XacifUtE",
        "START": "0x10000000000000000000",
        "END": "0x1fffffffffffffffffff"
    },
    "78": {
        "WALLET": "15qF6X51huDjqTmF9BJgxXdt1xcj46Jmhb",
        "START": "0x20000000000000000000",
        "END": "0x3fffffffffffffffffff"
    },
    "79": {
        "WALLET": "1ARk8HWJMn8js8tQmGUJeQHjSE7KRkn2t8",
        "START": "0x40000000000000000000",
        "END": "0x7fffffffffffffffffff"
    },
    "80": {
        "WALLET": "1BCf6rHUW6m3iH2ptsvnjgLruAiPQQepLe",
        "START": "0x80000000000000000000",
        "END": "0xffffffffffffffffffff"
    },
    "81": {
        "WALLET": "15qsCm78whspNQFydGJQk5rexzxTQopnHZ",
        "START": "0x100000000000000000000",
        "END": "0x1ffffffffffffffffffff"
    },
    "82": {
        "WALLET": "13zYrYhhJxp6Ui1VV7pqa5WDhNWM45ARAC",
        "START": "0x200000000000000000000",
        "END": "0x3ffffffffffffffffffff"
    },
    "83": {
        "WALLET": "14MdEb4eFcT3MVG5sPFG4jGLuHJSnt1Dk2",
        "START": "0x400000000000000000000",
        "END": "0x7ffffffffffffffffffff"
    },
    "84": {
        "WALLET": "1CMq3SvFcVEcpLMuuH8PUcNiqsK1oicG2D",
        "START": "0x800000000000000000000",
        "END": "0xfffffffffffffffffffff"
    },
    "85": {
        "WALLET": "1Kh22PvXERd2xpTQk3ur6pPEqFeckCJfAr",
        "START": "0x1000000000000000000000",
        "END": "0x1fffffffffffffffffffff"
    },
    "86": {
        "WALLET": "1K3x5L6G57Y494fDqBfrojD28UJv4s5JcK",
        "START": "0x2000000000000000000000",
        "END": "0x3fffffffffffffffffffff"
    },
    "87": {
        "WALLET": "1PxH3K1Shdjb7gSEoTX7UPDZ6SH4qGPrvq",
        "START": "0x4000000000000000000000",
        "END": "0x7fffffffffffffffffffff"
    },
    "88": {
        "WALLET": "16AbnZjZZipwHMkYKBSfswGWKDmXHjEpSf",
        "START": "0x8000000000000000000000",
        "END": "0xffffffffffffffffffffff"
    },
    "89": {
        "WALLET": "19QciEHbGVNY4hrhfKXmcBBCrJSBZ6TaVt",
        "START": "0x10000000000000000000000",
        "END": "0x1ffffffffffffffffffffff"
    },
    "90": {
        "WALLET": "1L12FHH2FHjvTviyanuiFVfmzCy46RRATU",
        "START": "0x20000000000000000000000",
        "END": "0x3ffffffffffffffffffffff"
    },
    "91": {
        "WALLET": "1EzVHtmbN4fs4MiNk3ppEnKKhsmXYJ4s74",
        "START": "0x40000000000000000000000",
        "END": "0x7ffffffffffffffffffffff"
    },
    "92": {
        "WALLET": "1AE8NzzgKE7Yhz7BWtAcAAxiFMbPo82NB5",
        "START": "0x80000000000000000000000",
        "END": "0xfffffffffffffffffffffff"
    },
    "93": {
        "WALLET": "17Q7tuG2JwFFU9rXVj3uZqRtioH3mx2Jad",
        "START": "0x100000000000000000000000",
        "END": "0x1fffffffffffffffffffffff"
    },
    "94": {
        "WALLET": "1K6xGMUbs6ZTXBnhw1pippqwK6wjBWtNpL",
        "START": "0x200000000000000000000000",
        "END": "0x3fffffffffffffffffffffff"
    },
    "95": {
        "WALLET": "19eVSDuizydXxhohGh8Ki9WY9KsHdSwoQC",
        "START": "0x400000000000000000000000",
        "END": "0x7fffffffffffffffffffffff"
    },
    "96": {
        "WALLET": "15ANYzzCp5BFHcCnVFzXqyibpzgPLWaD8b",
        "START": "0x800000000000000000000000",
        "END": "0xffffffffffffffffffffffff"
    },
    "97": {
        "WALLET": "18ywPwj39nGjqBrQJSzZVq2izR12MDpDr8",
        "START": "0x1000000000000000000000000",
        "END": "0x1ffffffffffffffffffffffff"
    },
    "98": {
        "WALLET": "1CaBVPrwUxbQYYswu32w7Mj4HR4maNoJSX",
        "START": "0x2000000000000000000000000",
        "END": "0x3ffffffffffffffffffffffff"
    },
    "99": {
        "WALLET": "1JWnE6p6UN7ZJBN7TtcbNDoRcjFtuDWoNL",
        "START": "0x4000000000000000000000000",
        "END": "0x7ffffffffffffffffffffffff"
    },
    "100": {
        "WALLET": "1KCgMv8fo2TPBpddVi9jqmMmcne9uSNJ5F",
        "START": "0x8000000000000000000000000",
        "END": "0xfffffffffffffffffffffffff"
    },
    "101": {
        "WALLET": "1CKCVdbDJasYmhswB6HKZHEAnNaDpK7W4n",
        "START": "0x10000000000000000000000000",
        "END": "0x1fffffffffffffffffffffffff"
    },
    "102": {
        "WALLET": "1PXv28YxmYMaB8zxrKeZBW8dt2HK7RkRPX",
        "START": "0x20000000000000000000000000",
        "END": "0x3fffffffffffffffffffffffff"
    },
    "103": {
        "WALLET": "1AcAmB6jmtU6AiEcXkmiNE9TNVPsj9DULf",
        "START": "0x40000000000000000000000000",
        "END": "0x7fffffffffffffffffffffffff"
    },
    "104": {
        "WALLET": "1EQJvpsmhazYCcKX5Au6AZmZKRnzarMVZu",
        "START": "0x80000000000000000000000000",
        "END": "0xffffffffffffffffffffffffff"
    },
    "105": {
        "WALLET": "1CMjscKB3QW7SDyQ4c3C3DEUHiHRhiZVib",
        "START": "0x100000000000000000000000000",
        "END": "0x1ffffffffffffffffffffffffff"
    },
    "106": {
        "WALLET": "18KsfuHuzQaBTNLASyj15hy4LuqPUo1FNB",
        "START": "0x200000000000000000000000000",
        "END": "0x3ffffffffffffffffffffffffff"
    },
    "107": {
        "WALLET": "15EJFC5ZTs9nhsdvSUeBXjLAuYq3SWaxTc",
        "START": "400000000000000000000000000",
        "END": "0x7ffffffffffffffffffffffffff"
    },
    "108": {
        "WALLET": "1HB1iKUqeffnVsvQsbpC6dNi1XKbyNuqao",
        "START": "0x800000000000000000000000000",
        "END": "0xfffffffffffffffffffffffffff"
    },
    "109": {
        "WALLET": "1GvgAXVCbA8FBjXfWiAms4ytFeJcKsoyhL",
        "START": "0x1000000000000000000000000000",
        "END": "0x1fffffffffffffffffffffffffff"
    },
    "110": {
        "WALLET": "12JzYkkN76xkwvcPT6AWKZtGX6w2LAgsJg",
        "START": "0x2000000000000000000000000000",
        "END": "0x3fffffffffffffffffffffffffff"
    },
    "111": {
        "WALLET": "1824ZJQ7nKJ9QFTRBqn7z7dHV5EGpzUpH3",
        "START": "0x4000000000000000000000000000",
        "END": "0x7fffffffffffffffffffffffffff"
    },
    "112": {
        "WALLET": "18A7NA9FTsnJxWgkoFfPAFbQzuQxpRtCos",
        "START": "0x8000000000000000000000000000",
        "END": "0xffffffffffffffffffffffffffff"
    },
    "113": {
        "WALLET": "1NeGn21dUDDeqFQ63xb2SpgUuXuBLA4WT4",
        "START": "0x10000000000000000000000000000",
        "END": "0x1ffffffffffffffffffffffffffff"
    },
    "114": {
        "WALLET": "174SNxfqpdMGYy5YQcfLbSTK3MRNZEePoy",
        "START": "0x20000000000000000000000000000",
        "END": "0x3ffffffffffffffffffffffffffff"
    },
    "115": {
        "WALLET": "1NLbHuJebVwUZ1XqDjsAyfTRUPwDQbemfv",
        "START": "0x40000000000000000000000000000",
        "END": "0x7ffffffffffffffffffffffffffff"
    },
    "116": {
        "WALLET": "1MnJ6hdhvK37VLmqcdEwqC3iFxyWH2PHUV",
        "START": "0x80000000000000000000000000000",
        "END": "0xfffffffffffffffffffffffffffff"
    },
    "117": {
        "WALLET": "1KNRfGWw7Q9Rmwsc6NT5zsdvEb9M2Wkj5Z",
        "START": "0x100000000000000000000000000000",
        "END": "0x1fffffffffffffffffffffffffffff"
    },
    "118": {
        "WALLET": "1PJZPzvGX19a7twf5HyD2VvNiPdHLzm9F6",
        "START": "0x200000000000000000000000000000",
        "END": "0x3fffffffffffffffffffffffffffff"
    },
    "119": {
        "WALLET": "1GuBBhf61rnvRe4K8zu8vdQB3kHzwFqSy7",
        "START": "0x400000000000000000000000000000",
        "END": "0x7fffffffffffffffffffffffffffff"
    },
    "120": {
        "WALLET": "17s2b9ksz5y7abUm92cHwG8jEPCzK3dLnT",
        "START": "0x800000000000000000000000000000",
        "END": "0xffffffffffffffffffffffffffffff"
    },
    "121": {
        "WALLET": "1GDSuiThEV64c166LUFC9uDcVdGjqkxKyh",
        "START": "0x1000000000000000000000000000000",
        "END": "0x1ffffffffffffffffffffffffffffff"
    },
    "122": {
        "WALLET": "1Me3ASYt5JCTAK2XaC32RMeH34PdprrfDx",
        "START": "0x2000000000000000000000000000000",
        "END": "0x3ffffffffffffffffffffffffffffff"
    },
    "123": {
        "WALLET": "1CdufMQL892A69KXgv6UNBD17ywWqYpKut",
        "START": "0x4000000000000000000000000000000",
        "END": "0x7ffffffffffffffffffffffffffffff"
    },
    "124": {
        "WALLET": "1BkkGsX9ZM6iwL3zbqs7HWBV7SvosR6m8N",
        "START": "0x8000000000000000000000000000000",
        "END": "0xfffffffffffffffffffffffffffffff"
    },
    "125": {
        "WALLET": "1PXAyUB8ZoH3WD8n5zoAthYjN15yN5CVq5",
        "START": "0x10000000000000000000000000000000",
        "END": "0x1fffffffffffffffffffffffffffffff"
    },
    "126": {
        "WALLET": "1AWCLZAjKbV1P7AHvaPNCKiB7ZWVDMxFiz",
        "START": "0x20000000000000000000000000000000",
        "END": "0x3fffffffffffffffffffffffffffffff"
    },
    "127": {
        "WALLET": "1G6EFyBRU86sThN3SSt3GrHu1sA7w7nzi4",
        "START": "0x40000000000000000000000000000000",
        "END": "0x7fffffffffffffffffffffffffffffff"
    },
    "128": {
        "WALLET": "1MZ2L1gFrCtkkn6DnTT2e4PFUTHw9gNwaj",
        "START": "0x80000000000000000000000000000000",
        "END": "0xffffffffffffffffffffffffffffffff"
    },
    "129": {
        "WALLET": "1Hz3uv3nNZzBVMXLGadCucgjiCs5W9vaGz",
        "START": "0x100000000000000000000000000000000",
        "END": "0x1ffffffffffffffffffffffffffffffff"
    },
    "130": {
        "WALLET": "1Fo65aKq8s8iquMt6weF1rku1moWVEd5Ua",
        "START": "0x200000000000000000000000000000000",
        "END": "0x3ffffffffffffffffffffffffffffffff"
    },
    "131": {
        "WALLET": "16zRPnT8znwq42q7XeMkZUhb1bKqgRogyy",
        "START": "0x400000000000000000000000000000000",
        "END": "0x7ffffffffffffffffffffffffffffffff"
    },
    "132": {
        "WALLET": "1KrU4dHE5WrW8rhWDsTRjR21r8t3dsrS3R",
        "START": "0x800000000000000000000000000000000",
        "END": "0xfffffffffffffffffffffffffffffffff"
    },
    "133": {
        "WALLET": "17uDfp5r4n441xkgLFmhNoSW1KWp6xVLD",
        "START": "0x1000000000000000000000000000000000",
        "END": "0x1fffffffffffffffffffffffffffffffff"
    },
    "134": {
        "WALLET": "13A3JrvXmvg5w9XGvyyR4JEJqiLz8ZySY3",
        "START": "0x2000000000000000000000000000000000",
        "END": "0x3fffffffffffffffffffffffffffffffff"
    },
    "135": {
        "WALLET": "16RGFo6hjq9ym6Pj7N5H7L1NR1rVPJyw2v",
        "START": "0x4000000000000000000000000000000000",
        "END": "0x7fffffffffffffffffffffffffffffffff"
    },
    "136": {
        "WALLET": "1UDHPdovvR985NrWSkdWQDEQ1xuRiTALq",
        "START": "0x8000000000000000000000000000000000",
        "END": "0xffffffffffffffffffffffffffffffffff"
    },
    "137": {
        "WALLET": "15nf31J46iLuK1ZkTnqHo7WgN5cARFK3RA",
        "START": "0x10000000000000000000000000000000000",
        "END": "0x1ffffffffffffffffffffffffffffffffff"
    },
    "138": {
        "WALLET": "1Ab4vzG6wEQBDNQM1B2bvUz4fqXXdFk2WT",
        "START": "0x20000000000000000000000000000000000",
        "END": "0x3ffffffffffffffffffffffffffffffffff"
    },
    "139": {
        "WALLET": "1Fz63c775VV9fNyj25d9Xfw3YHE6sKCxbt",
        "START": "0x40000000000000000000000000000000000",
        "END": "0x7ffffffffffffffffffffffffffffffffff"
    },
    "140": {
        "WALLET": "1QKBaU6WAeycb3DbKbLBkX7vJiaS8r42Xo",
        "START": "0x80000000000000000000000000000000000",
        "END": "0xfffffffffffffffffffffffffffffffffff"
    },
    "141": {
        "WALLET": "1CD91Vm97mLQvXhrnoMChhJx4TP9MaQkJo",
        "START": "0x100000000000000000000000000000000000",
        "END": "0x1fffffffffffffffffffffffffffffffffff"
    },
    "142": {
        "WALLET": "15MnK2jXPqTMURX4xC3h4mAZxyCcaWWEDD",
        "START": "0x200000000000000000000000000000000000",
        "END": "0x3fffffffffffffffffffffffffffffffffff"
    },
    "143": {
        "WALLET": "13N66gCzWWHEZBxhVxG18P8wyjEWF9Yoi1",
        "START": "0x400000000000000000000000000000000000",
        "END": "0x7fffffffffffffffffffffffffffffffffff"
    },
    "144": {
        "WALLET": "1NevxKDYuDcCh1ZMMi6ftmWwGrZKC6j7Ux",
        "START": "0x800000000000000000000000000000000000",
        "END": "0xffffffffffffffffffffffffffffffffffff"
    },
    "145": {
        "WALLET": "19GpszRNUej5yYqxXoLnbZWKew3KdVLkXg",
        "START": "0x1000000000000000000000000000000000000",
        "END": "0x1ffffffffffffffffffffffffffffffffffff"
    },
    "146": {
        "WALLET": "1M7ipcdYHey2Y5RZM34MBbpugghmjaV89P",
        "START": "0x2000000000000000000000000000000000000",
        "END": "0x3ffffffffffffffffffffffffffffffffffff"
    },
    "147": {
        "WALLET": "18aNhurEAJsw6BAgtANpexk5ob1aGTwSeL",
        "START": "0x4000000000000000000000000000000000000",
        "END": "0x7ffffffffffffffffffffffffffffffffffff"
    },
    "148": {
        "WALLET": "1FwZXt6EpRT7Fkndzv6K4b4DFoT4trbMrV",
        "START": "0x8000000000000000000000000000000000000",
        "END": "0xfffffffffffffffffffffffffffffffffffff"
    },
    "149": {
        "WALLET": "1CXvTzR6qv8wJ7eprzUKeWxyGcHwDYP1i2",
        "START": "0x10000000000000000000000000000000000000",
        "END": "0x1fffffffffffffffffffffffffffffffffffff"
    },
    "150": {
        "WALLET": "1MUJSJYtGPVGkBCTqGspnxyHahpt5Te8jy",
        "START": "0x20000000000000000000000000000000000000",
        "END": "0x3fffffffffffffffffffffffffffffffffffff"
    },
    "151": {
        "WALLET": "13Q84TNNvgcL3HJiqQPvyBb9m4hxjS3jkV",
        "START": "0x40000000000000000000000000000000000000",
        "END": "0x7fffffffffffffffffffffffffffffffffffff"
    },
    "152": {
        "WALLET": "1LuUHyrQr8PKSvbcY1v1PiuGuqFjWpDumN",
        "START": "0x80000000000000000000000000000000000000",
        "END": "0xffffffffffffffffffffffffffffffffffffff"
    },
    "153": {
        "WALLET": "18192XpzzdDi2K11QVHR7td2HcPS6Qs5vg",
        "START": "0x100000000000000000000000000000000000000",
        "END": "0x1ffffffffffffffffffffffffffffffffffffff"
    },
    "154": {
        "WALLET": "1NgVmsCCJaKLzGyKLFJfVequnFW9ZvnMLN",
        "START": "0x200000000000000000000000000000000000000",
        "END": "0x3ffffffffffffffffffffffffffffffffffffff"
    },
    "155": {
        "WALLET": "1AoeP37TmHdFh8uN72fu9AqgtLrUwcv2wJ",
        "START": "0x400000000000000000000000000000000000000",
        "END": "0x7ffffffffffffffffffffffffffffffffffffff"
    },
    "156": {
        "WALLET": "1FTpAbQa4h8trvhQXjXnmNhqdiGBd1oraE",
        "START": "0x800000000000000000000000000000000000000",
        "END": "0xfffffffffffffffffffffffffffffffffffffff"
    },
    "157": {
        "WALLET": "14JHoRAdmJg3XR4RjMDh6Wed6ft6hzbQe9",
        "START": "0x1000000000000000000000000000000000000000",
        "END": "0x1fffffffffffffffffffffffffffffffffffffff"
    },
    "158": {
        "WALLET": "19z6waranEf8CcP8FqNgdwUe1QRxvUNKBG",
        "START": "0x2000000000000000000000000000000000000000",
        "END": "0x3fffffffffffffffffffffffffffffffffffffff"
    },
    "159": {
        "WALLET": "14u4nA5sugaswb6SZgn5av2vuChdMnD9E5",
        "START": "0x4000000000000000000000000000000000000000",
        "END": "0x7fffffffffffffffffffffffffffffffffffffff"
    },
    "160": {
        "WALLET": "1NBC8uXJy1GiJ6drkiZa1WuKn51ps7EPTv",
        "START": "0x8000000000000000000000000000000000000000",
        "END": "0xffffffffffffffffffffffffffffffffffffffff"
    }
}