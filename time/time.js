/**
 * Sleep(sync)
 * @param {*} ms delay
 */
function sleep(ms) {
    const wakeUpTime = Date.now() + ms;
    while (Date.now() < wakeUpTime) {}
}

/**
 * Delay
 * @param {*} ms delay
 */
function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

console.log('start');
sleep(3000)
console.log('end');
