function get_Time() {
    let now = new Date();
    let year = now.getFullYear();
    let month = now.getMonth() + 1;
    let date = now.getDate();

    let hour = now.getHours();
    let minutes = String(now.getMinutes()).padStart(2, "0");
    let seconds = String(now.getSeconds()).padStart(2, "0");

    return `${year}-${month}-${date} ${hour}:${minutes}:${seconds}`
}