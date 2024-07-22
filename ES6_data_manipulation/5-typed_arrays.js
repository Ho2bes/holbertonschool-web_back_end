export default function createInt8TypedArray(length, position, value) {
  if (position >= length) {
    throw Error('Position outside range');
  }
  const token = new ArrayBuffer(length);
  const dataView = new DataView(token);
  dataView.setInt8(position, value);
  return dataView;
}
