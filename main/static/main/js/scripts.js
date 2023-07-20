function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function sleep_time() {
  console.log("Start");
  await sleep(2000);
  console.log("After 2 seconds");
}