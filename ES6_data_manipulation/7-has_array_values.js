export default function has(set, array) {
  const check = array.every((item) => set.has(item));
  return check;
}
