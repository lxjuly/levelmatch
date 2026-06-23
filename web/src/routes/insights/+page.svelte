<script>
	import { api } from '$lib/api.js';

	let loading = $state(true);
	let error = $state('');
	let topSkills = $state([]);
	let topStack = $state([]);
	let total = $state(0);

	function tally(jobs, field) {
		const counts = {};
		for (const job of jobs) {
			for (const item of job[field] ?? []) {
				const key = item.trim();
				if (!key) continue;
				counts[key] = (counts[key] ?? 0) + 1;
			}
		}
		return Object.entries(counts)
			.map(([name, count]) => ({ name, count }))
			.sort((a, b) => b.count - a.count)
			.slice(0, 15);
	}

	async function load() {
		loading = true;
		error = '';
		try {
			const jobs = await api.listJobs({ limit: 100 });
			total = jobs.length;
			topSkills = tally(jobs, 'required_skills');
			topStack = tally(jobs, 'tech_stack');
		} catch (e) {
			error = e.message;
		} finally {
			loading = false;
		}
	}

	$effect(() => {
		load();
	});
</script>

<h1>Market insights</h1>
<p class="muted">Aggregated across {total} ingested postings.</p>

{#if loading}
	<p class="muted">Loading…</p>
{:else if error}
	<p class="error">{error}</p>
{:else}
	<div class="cols">
		<section>
			<h2>Most-demanded skills</h2>
			{#each topSkills as skill}
				<div class="bar-row">
					<span class="label">{skill.name}</span>
					<div class="bar">
						<div class="fill" style="width:{(skill.count / topSkills[0].count) * 100}%"></div>
					</div>
					<span class="count">{skill.count}</span>
				</div>
			{/each}
		</section>

		<section>
			<h2>Most-common tech stack</h2>
			{#each topStack as t}
				<div class="bar-row">
					<span class="label">{t.name}</span>
					<div class="bar">
						<div class="fill stack" style="width:{(t.count / topStack[0].count) * 100}%"></div>
					</div>
					<span class="count">{t.count}</span>
				</div>
			{/each}
		</section>
	</div>
{/if}

<style>
	.muted {
		color: #8b949e;
	}
	.error {
		color: #f85149;
	}
	.cols {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 2rem;
		margin-top: 1.5rem;
	}
	h2 {
		font-size: 1rem;
		margin-bottom: 1rem;
	}
	.bar-row {
		display: grid;
		grid-template-columns: 140px 1fr 32px;
		align-items: center;
		gap: 0.6rem;
		margin-bottom: 0.5rem;
	}
	.label {
		font-size: 0.85rem;
		white-space: nowrap;
		overflow: hidden;
		text-overflow: ellipsis;
	}
	.bar {
		background: #161b22;
		border-radius: 4px;
		height: 18px;
		overflow: hidden;
	}
	.fill {
		height: 100%;
		background: #58a6ff;
		border-radius: 4px;
	}
	.fill.stack {
		background: #a371f7;
	}
	.count {
		font-size: 0.8rem;
		color: #8b949e;
		text-align: right;
	}
	@media (max-width: 700px) {
		.cols {
			grid-template-columns: 1fr;
		}
	}
</style>
