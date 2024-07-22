export default function createIn8TypedArray(length, position, value) {
  if (position >= length) {
    throw new Error('Position outside range');
  }
  const buffer = new ArrayBuffer(length);
  const view = new view(buffer);
  view.setInt8(position, value);
  return view;
}
