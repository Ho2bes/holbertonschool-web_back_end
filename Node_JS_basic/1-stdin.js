// Affiche le message de bienvenue
console.log("Welcome to Holberton School, what is your name?");

// Écoute l'entrée standard (stdin) de l'utilisateur
process.stdin.on('data', (input) => {
  // Supprime les espaces autour de l'entrée
  const name = input.toString().trim();

  // Affiche le nom de l'utilisateur
  console.log(`Your name is: ${name}`);

  // Fin du programme
  process.stdin.end();
});

// Événement pour la fin de l'entrée
process.stdin.on('end', () => {
  console.log("This important software is now closing");
});
