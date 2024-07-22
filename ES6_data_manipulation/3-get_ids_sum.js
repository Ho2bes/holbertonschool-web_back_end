export default function getStudentIdsSum(array) {
  if (!Array.isArray(array)) {
    return 0;
  }
  return array.reduce((accumulator, student) => accumulator + student.id, 0);
}
