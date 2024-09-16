// Affiche le message initial
console.log("Welcome to Holberton School, what is your name?");

// Capture l'entrée de l'utilisateur via le flux stdin
process.stdin.on('data', (input) => {
  // Convertit l'entrée en chaîne de caractères et enlève les espaces vides
  const name = input.toString().trim();

  // Affiche le message avec le nom de l'utilisateur
  console.log(`Your name is: ${name}`);

  // Indique que le programme est en train de se terminer
  console.log("This important software is now closing");

  // Ferme le processus
  process.exit();
});
