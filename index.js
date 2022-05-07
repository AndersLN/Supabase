const h1 = document.querySelector("h1")
const btn = document.querySelector("button")



const handleClick = () => {
    h1.style.color = "red"
}
btn.addEventListener("click",handleClick)
