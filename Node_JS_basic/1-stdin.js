// Affiche le message de bienvenue
console.log("Welcome to Holberton School, what is your name?");

// Écoute l'entrée standard (stdin) de l'utilisateur
process.stdin.on('data', (input) => {
  const name = input.toString().trim();
  console.log(`Your name is: ${name}`);
});

// Événement pour la fin de l'entrée
process.stdin.on('end', () => {
  console.log("This important software is now closing");
});
