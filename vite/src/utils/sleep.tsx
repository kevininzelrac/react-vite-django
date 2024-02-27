const sleep = (delay = 200) =>
  new Promise((resolve) => setTimeout(resolve, delay));
export default sleep;
