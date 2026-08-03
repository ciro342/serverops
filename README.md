# ServerOps

Proyecto personal de aprendizaje: una CLI en Python para administrar servidores Linux (inventario, SSH, servicios, logs y Docker).

Lo estoy construyendo poco a poco, fase por fase, para entender bien cómo se diseña una herramienta de infraestructura desde cero — no es un proyecto terminado, sigue en desarrollo.

## Tecnologías usadas

- **Python**
- **Typer** — framework para construir la CLI
- **Rich** — salida en terminal con tablas y colores
- **PyYAML** — inventario de servidores en YAML
- **Paramiko** — conexión SSH
- **logging** — registro de eventos
- **Docker** — entorno de pruebas

## Estructura

```
serverops/
├── cli.py
├── config/
│   ├── inventory.yml
│   └── servers.log
├── commands/
│   ├── inventory.py
│   ├── ssh.py
│   ├── service.py
│   ├── logs.py
│   └── docker.py
├── core/
│   ├── ssh_client.py
│   └── logger.py
├── models/
│   └── server.py
├── tests/
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Fases

- [x] **Fase 1 — Inventario**: agregar, listar, editar y eliminar servidores (YAML)
- [X] **Fase 2 — SSH**: conexión remota vía Paramiko *(en progreso)*
- [X] **Fase 3 — Servicios**: status/restart de servicios remotos
- [X] **Fase 4 — Logs**: ver logs de servicios remotos
- [ ] **Fase 5 — Monitoreo**: CPU, RAM, disco, load average
- [ ] **Fase 6 — Docker**: control de contenedores remotos

## Comandos (por ahora)

```bash
python3 cli.py inventory add <nombre> <ip> <usuario> <puerto>
python3 cli.py inventory listall
python3 cli.py inventory remove <nombre>
python3 cli.py inventory update <nombre> <campo> <valor>
```

## Instalación

```bash
git clone <url-del-repo>
cd serverops
pip install -r requirements.txt
```

---

Proyecto en construcción — Zero
