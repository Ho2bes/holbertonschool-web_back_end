const express = require('express');

// Créer l'application Express
const app = express();

// Définir la route pour "/"
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Le serveur écoute sur le port 1245
app.listen(1245, () => {
  console.log('Server listening on port 1245');
});

// Exporter l'application pour d'éventuels tests ou utilisation
module.exports = app;
