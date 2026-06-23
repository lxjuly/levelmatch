<script>
	import { page } from '$app/state';
	import { api } from '$lib/api.js';
	import { activeProfile } from '$lib/profile.svelte.js';

	let job = $state(null);
	let gap = $state(null);
	let loading = $state(true);
	let error = $state('');

	const jobId = page.params.id;

	async function load() {
		loading = true;
		error = '';
		try {
			job = await api.getJob(jobId);
			if (activeProfile.id) {
				gap = await api.gapForJob(jobId, activeProfile.id);
			}
		} catch (e) {
			error = e.message;
		} finally {
			loading = false;
		}
	}

	function scoreColor(score) {
		if (score >= 0.6) return '#4ac26b';
		if (score >= 0.3) return '#d29922';
		return '#f85149';
	}

	$effect(() => {
		load();
	});
</script>

<a class="back" href="/">← All jobs</a>

{#if loading}
	<p class="muted">Loading…</p>
{:else if error}
	<p class="error">{error}</p>
{:else if job}
	<h1>{job.title}</h1>
	<p class="sub">{job.company} · {job.location}</p>

	<div class="meta">
		{#if job.seniority_level}<span class="tag">{job.seniority_level}</span>{/if}
		{#if job.role_type}<span class="tag">{job.role_type}</span>{/if}
		{#if job.remote_type}<span class="tag">{job.remote_type}</span>{/if}
		{#if job.years_experience != null}<span class="tag">{job.years_experience}+ yrs</span>{/if}
		{#if job.salary_min}<span class="tag">${job.salary_min / 1000}k–${job.salary_max / 1000}k</span>{/if}
	</div>

	{#if gap}
		<div class="gap-card">
			<div class="gap-head">
				<div class="score" style="color:{scoreColor(gap.match_score)}">
					{Math.round(gap.match_score * 100)}%
					<span>match</span>
				</div>
				<div class="fits">
					<span class="fit">Seniority: <b>{gap.seniority_fit}</b></span>
					<span class="fit">Role match: <b>{gap.role_type_match ? 'yes' : 'no'}</b></span>
				</div>
			</div>
			{#if gap.summary}<p class="summary">{gap.summary}</p>{/if}
			{#if gap.missing_required.length}
				<h3>Missing required skills</h3>
				<div class="chips">
					{#each gap.missing_required as skill}<span class="chip miss">{skill}</span>{/each}
				</div>
			{/if}
			{#if gap.missing_preferred.length}
				<h3>Missing preferred skills</h3>
				<div class="chips">
					{#each gap.missing_preferred as skill}<span class="chip">{skill}</span>{/each}
				</div>
			{/if}
		</div>
	{:else if !activeProfile.id}
		<p class="hint"><a href="/profile">Create a profile</a> to see your gap report for this role.</p>
	{/if}

	<h3>Required skills</h3>
	<div class="chips">
		{#each job.required_skills as skill}<span class="chip">{skill}</span>{/each}
	</div>

	{#if job.tech_stack?.length}
		<h3>Tech stack</h3>
		<div class="chips">
			{#each job.tech_stack as t}<span class="chip">{t}</span>{/each}
		</div>
	{/if}
{/if}

<style>
	.back {
		color: #58a6ff;
		text-decoration: none;
		font-size: 0.9rem;
	}
	h1 {
		margin: 1rem 0 0.25rem;
	}
	.sub {
		color: #8b949e;
		margin: 0 0 1rem;
	}
	.meta {
		display: flex;
		flex-wrap: wrap;
		gap: 0.5rem;
		margin-bottom: 1.5rem;
	}
	.tag {
		background: #21262d;
		color: #c9d1d9;
		padding: 0.2rem 0.6rem;
		border-radius: 999px;
		font-size: 0.8rem;
	}
	.gap-card {
		background: #161b22;
		border: 1px solid #30363d;
		border-radius: 10px;
		padding: 1.25rem;
		margin-bottom: 1.5rem;
	}
	.gap-head {
		display: flex;
		align-items: center;
		gap: 1.5rem;
	}
	.score {
		font-size: 2rem;
		font-weight: 800;
		line-height: 1;
	}
	.score span {
		font-size: 0.8rem;
		font-weight: 500;
		color: #8b949e;
		display: block;
	}
	.fits {
		display: flex;
		flex-direction: column;
		gap: 0.25rem;
		font-size: 0.9rem;
		color: #8b949e;
	}
	.summary {
		margin: 1rem 0 0;
		font-style: italic;
		color: #c9d1d9;
	}
	h3 {
		font-size: 0.85rem;
		text-transform: uppercase;
		letter-spacing: 0.04em;
		color: #8b949e;
		margin: 1.25rem 0 0.5rem;
	}
	.chips {
		display: flex;
		flex-wrap: wrap;
		gap: 0.4rem;
	}
	.chip {
		background: #21262d;
		padding: 0.25rem 0.6rem;
		border-radius: 6px;
		font-size: 0.85rem;
	}
	.chip.miss {
		background: #3d1417;
		color: #ff7b72;
	}
	.hint a,
	.error {
		color: #58a6ff;
	}
	.muted {
		color: #8b949e;
	}
	.error {
		color: #f85149;
	}
</style>
