import App from './App.svelte';

window.socket = io();

const app = new App({
	target: document.body,
});

export default app;