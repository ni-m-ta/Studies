// List A
const listA = [1, 2, 3, 4, 5];

// List B
const listB = [2, 4];

// Eliminate elements from list A that belong to list B
const result = listA.filter(item => listB.includes(item));

console.log(result);