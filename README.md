# sensor-gateway

Projeto IoT utilizando Raspberry Pi para coleta de dados de sensores Grove usando o Grove Base HAT.

# Configuração do Raspberry Pi

## 1. Habilitar I2C

Executar:

```bash
sudo raspi-config
```

Depois acessar:

```text
Interface Options -> I2C -> Enable
```

Reiniciar o Raspberry:

```bash
sudo reboot
```

---

## 2. Instalar ferramentas I2C

```bash
sudo apt update
sudo apt install i2c-tools
```

Verificar dispositivos conectados:

```bash
sudo i2cdetect -y 1
```

Durante os testes o Grove Base HAT foi identificado no endereço:

```text
0x08
```

Importante: ao rodar no seu Raspberry, verifique qual endereço foi identificado, pois isso pode ser importante nos próximos passos.

---

# Instalação do Projeto

## 1. Clonar o projeto

```bash
git clone <https://github.com/HevelinFR/sensor-gateway.git>
cd sensor-gateway
```

---

## 2. Criar ambiente virtual

```bash
python3 -m venv venv
```

Ativar ambiente virtual:

```bash
source venv/bin/activate
```

---

## 3. Instalar dependências do projeto

```bash
pip install -r requirements.txt
```

---

# Instalação da biblioteca grove.py

A biblioteca `grove.py` deve ser clonada separadamente do projeto `sensor-gateway`.

Estrutura recomendada:

```text
/home/pi/
├── sensor-gateway/
└── grove.py/
```

Clonar a biblioteca:

```bash
cd /home/pi

git clone https://github.com/Seeed-Studio/grove.py
```

Entrar na pasta:

```bash
cd grove.py
```

---

# Ajuste da biblioteca grove.py

Importante: esse ajuste deve ser feito antes de instalar a biblioteca no ambiente virtual.

Ao utilizar a biblioteca [grove.py](https://github.com/seeed-studio/grove.py), o endereço padrão do ADC estava configurado como:

```python
address = 0x04
```

Porém, o Grove Base HAT pode estar em outro endereço, como o identificado anteriormente com o `i2cdetect`.

No meu Raspberry Pi 4 o endereço identificado foi:

```text
0x08
```

Foi necessário alterar o arquivo:

```text
grove.py/grove/adc.py
```

Trecho alterado:

```python
class ADC(object):

    def __init__(self, address = 0x08):
```

---

# Instalar grove.py no ambiente virtual

Ativar o ambiente virtual do projeto:

```bash
source ../sensor-gateway/venv/bin/activate
```

Instalar a biblioteca localmente:

```bash
pip install .
```

Após isso os módulos `grove` estarão disponíveis dentro do ambiente virtual do projeto `sensor-gateway`.

# Executando o Projeto

Ativar o ambiente virtual:

```bash
source venv/bin/activate
```

Executar o menu principal do projeto:

```bash
python -m app.main
```

Ao executar o comando, um menu será exibido no terminal.

Exemplo:

```text
O que deseja fazer?

[1] - Testar sensores
```

Selecionando a opção de teste de sensores:

```text
Qual sensor deseja testar?

[1] - Sensor de luminosidade
```

Atualmente o projeto possui suporte para teste do:

* Grove Light Sensor v1.2

Conectado na porta:

```text
A0
```

Após selecionar o sensor, os valores lidos serão exibidos no terminal em tempo real.

