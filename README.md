# elite-tool

## WTF is this

A simple, dirty and quick tool for a friend's repairment shop.

## Usage

Run the server with:

```bash
git clone https://github.com/gorcajo/elite-tool.git
cd elite-tool
sudo ./run.sh
```

And then you can browse to <http://localhost/pages/new>

## To Do List

- Añadir campos a la entidad repairment:
  - backup
  - password
  - withdrawal_date
- Validación de campos en el front
- Usar fechas como está mandao
- Darle una vuelta a pdf.py, es una basura de código
- Darle una vuelta a los html, hay mucho código repetido entre ficheros (handlebars.js?)
- Añadir una página de configuración (para por ejemplo, la plantilla PDF)
- Cuando el usuario crea o edita una reparación, llevarle al PDF
- En el navbar poner el logo
- Guardar logs rotativos en disco
- Bug: Quitar el link al pulsar en el título del navbar, o al menos que nos lleve al root de la web (hace cosas raras)
