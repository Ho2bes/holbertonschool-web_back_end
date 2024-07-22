export function hasValuesFromArray(set, array) {
  return array.every((value) => set.has(value));
}
