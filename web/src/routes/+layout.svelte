<script>
	import favicon from '$lib/assets/favicon.svg';
	import { page } from '$app/state';
	import { activeProfile } from '$lib/profile.svelte.js';

	let { children } = $props();

	const links = [
		{ href: '/', label: 'Jobs' },
		{ href: '/insights', label: 'Insights' },
		{ href: '/profile', label: 'Profile' }
	];
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
	<title>LevelMatch</title>
</svelte:head>

<div class="app">
	<header>
		<a class="brand" href="/">Level<span>Match</span></a>
		<nav>
			{#each links as link}
				<a href={link.href} class:active={page.url.pathname === link.href}>{link.label}</a>
			{/each}
		</nav>
		<span class="profile-chip" class:set={activeProfile.id}>
			{activeProfile.id ? 'Profile active' : 'No profile'}
		</span>
	</header>
	<main>
		{@render children()}
	</main>
</div>

<style>
	:global(body) {
		margin: 0;
		font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
		background: #0d1117;
		color: #e6edf3;
	}

	:global(*) {
		box-sizing: border-box;
	}

	.app {
		max-width: 1000px;
		margin: 0 auto;
		padding: 0 1.5rem;
	}

	header {
		display: flex;
		align-items: center;
		gap: 1.5rem;
		padding: 1.25rem 0;
		border-bottom: 1px solid #21262d;
	}

	.brand {
		font-size: 1.25rem;
		font-weight: 700;
		text-decoration: none;
		color: #e6edf3;
	}
	.brand span {
		color: #58a6ff;
	}

	nav {
		display: flex;
		gap: 1rem;
		flex: 1;
	}
	nav a {
		text-decoration: none;
		color: #8b949e;
		font-weight: 500;
		padding: 0.25rem 0;
		border-bottom: 2px solid transparent;
	}
	nav a:hover {
		color: #e6edf3;
	}
	nav a.active {
		color: #e6edf3;
		border-bottom-color: #58a6ff;
	}

	.profile-chip {
		font-size: 0.8rem;
		padding: 0.25rem 0.6rem;
		border-radius: 999px;
		background: #21262d;
		color: #8b949e;
	}
	.profile-chip.set {
		background: #133a1e;
		color: #4ac26b;
	}

	main {
		padding: 2rem 0;
	}
</style>
