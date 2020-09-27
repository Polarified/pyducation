const gc = document.getElementById("gc")
const ctx = gc.getContext("2d")
const board_border = 'black';
const board_background = "white";
const snake_col = 'lightblue';
const snake_border = 'darkblue';
apple_col = 'lightgreen'
apple_border = 'darkgreen'


let snake = [
      {x: 200, y: 200},
      {x: 200, y: 190}
    ]
let vx = 10;
let vy = 0;
let food = {x: 0, y: 0};
let score = 0;
let game_speed = 100;

function drawSnakePart(snakePart) {
    ctx.fillStyle = snake_col;
    ctx.strokeStyle = snake_border;
    ctx.fillRect(snakePart.x, snakePart.y, 10, 10)
    ctx.strokeRect(snakePart.x, snakePart.y, 10, 10)
}

function drawSnake() {
    snake.forEach(drawSnakePart)
}

function genFood() {
    food = {x:Math.round(Math.random() * (gc.width-10) / 10) * 10, y:Math.round(Math.random() * (gc.height-10) / 10) * 10}
    snake.forEach(function(part){
        if (part === food) {
            genFood();
        }
    })
}

function drawFood() {
    ctx.fillStyle = apple_col;
    ctx.strokeStyle = apple_border;
    ctx.fillRect(food.x, food.y, 10, 10)
    ctx.strokeRect(food.x, food.y, 10, 10)
}

function moveSnake() {
    let head = {x: (gc.width + snake[0].x + vx) % gc.width, y: (gc.height + snake[0].y + vy) % gc.height}
    snake.unshift(head)
    if (head.x === food.x && head.y === food.y) {
        score += 10
        game_speed *= 0.95;
        document.getElementById('score').innerHTML = score;
        genFood()
    } else {
        snake.pop()
    }
}

document.addEventListener("keydown", function(event) {
    const goingUp = vy === -10
    const goingDown = vy === 10
    const goingLeft = vx === -10
    const goingRight = vx === 10

    if (event.key === "w" && !goingDown) {
        vx = 0;
        vy = -10;
    }
    if (event.key === "a" && !goingRight) {
        vx = -10;
        vy = 0;
    }
    if (event.key === "s" && !goingUp) {
        vx = 0;
        vy = 10;
    }
    if (event.key === "d" && !goingLeft) {
        vx = 10;
        vy = 0;
    }
});

function clearCanvas() {
      ctx.fillStyle = board_background;
      ctx.strokestyle = board_border;
      ctx.fillRect(0, 0, gc.width, gc.height);
      ctx.strokeRect(0, 0, gc.width, gc.height);
}

function gameOver() {
    for (let i = 1; i< snake.length; i++) {
        if (snake[i].x === snake[0].x && snake[i].y === snake[0].y) {
            document.getElementById("score").innerHTML = "Game Over, your score was: "+ score;
            return true;
        }
    }
    return false;
}

function main() {
    if (gameOver()) {
        return;
    }
    setTimeout(function onTick() {
        clearCanvas();
        drawFood();
        moveSnake();
        drawSnake();
        // Call main again
        main();
    }, game_speed)
}

main();