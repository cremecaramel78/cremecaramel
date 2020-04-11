<script>
import Frames from './Frames.svelte';

let frames = [
	{server: '691144859142062181', channel: '691144859142062184'}
];

</script>

<main>
	<h1 class="glow">Creme Caramel</h1>

	<div id="servers">
		<p class="glow" style="font-weight: normal; font-size: 30px;">SERVERS</p>
		{#each frames as f}
			<Frames link={f.server} channel={f.channel} />
		{/each}
	</div>
</main>

<style>

	#servers{
		padding: 10px;
		background: #202c38;
		border-radius: 10px;
	}

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