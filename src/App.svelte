<script>

window.socket.on('connect', ()=>{
	window.socket.emit('user connected', 12345)
})

</script>

<main>
	<h1 class="glow">Hello Creme!</h1>
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #6EDBFF;
		font-weight: bold;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}

	.glow {
  font-size: 80px;
  color: #6EDBFF;
  text-align: center;
  -webkit-animation: glow 1s ease-in-out infinite alternate;
  -moz-animation: glow 1s ease-in-out infinite alternate;
  animation: glow 1s ease-in-out infinite alternate;
}

@keyframes glow {
  from {
    text-shadow: 0 0 10px #6EDBFF, 0 0 20px #6EDBFF, 0 0 30px #b3ecff, 0 0 40px #b3ecff, 0 0 50px #b3ecff, 0 0 60px #b3ecff, 0 0 70px #b3ecff;
  }
  to {
    text-shadow: 0 0 20px #6EDBFF, 0 0 30px #1ac6ff, 0 0 40px #1ac6ff, 0 0 50px #1ac6ff, 0 0 60px #1ac6ff, 0 0 70px #1ac6ff, 0 0 80px #1ac6ff;
  }
}
</style>