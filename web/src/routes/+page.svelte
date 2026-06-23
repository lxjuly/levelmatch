<script>
	import { api } from '$lib/api.js';
	import { activeProfile } from '$lib/profile.svelte.js';

	let jobs = $state([]);
	let gapByJob = $state({});
	let loading = $state(true);
	let error = $state('');

	let ingestQuery = $state('AI Engineer');
	let ingesting = $state(false);
	let ingestResult = $state('');

	async function load() {
		loading = true;
		error = '';
		try {
			jobs = await api.listJobs({ limit: 50 });
			if (activeProfile.id) {
				const reports = await api.gapBatch({ profileId: activeProfile.id, limit: 50 });
				const map = {};
				for (const r of reports) map[r.job_posting_id] = r;
				gapByJob = map;
			} else {
				gapByJob = {};
			}
		} catch (e) {
			error = e.message;
		} finally {
			loading = false;
		}
	}

	async function runIngest() {
		ingesting = true;
		ingestResult = '';
		try {
			const res = await api.ingest(ingestQuery, 1);
			ingestResult = `+${res.created} new, ${res.skipped} skipped`;
			await load();
		} catch (e) {
			ingestResult = `Error: ${e.message}`;
		} finally {
			ingesting = false;
		}
	}

	function scoreColor(score) {
		if (score >= 0.6) return '#4ac26b';
		if (score >= 0.3) return '#d29922';
		return '#f85149';
	}

	$effect(() => {
		// reload when the active profile changes
		activeProfile.id;
		load();
	});
</script>

<section class="ingest">
	<input
		bind:value={ingestQuery}
		placeholder="Search query, e.g. AI Engineer"
		onkeydown={(e) => e.key === 'Enter' && runIngest()}
	/>
	<button onclick={runIngest} disabled={ingesting}>
		{ingesting ? 'Ingesting…' : 'Ingest jobs'}
	</button>
	{#if ingestResult}<span class="ingest-result">{ingestResult}</span>{/if}
</section>

{#if !activeProfile.id}
	<p class="hint">
		No profile set — <a href="/profile">create one</a> to see how you match each role.
	</p>
{/if}

{#if loading}
	<p class="muted">Loading jobs…</p>
{:else if error}
	<p class="error">{error}</p>
{:else if jobs.length === 0}
	<p class="muted">No jobs yet. Run an ingest above to fetch some.</p>
{:else}
	<table>
		<thead>
			<tr>
				<th>Role</th>
				<th>Company</th>
				<th>Level</th>
				<th>Location</th>
				{#if activeProfile.id}<th class="num">Match</th>{/if}
			</tr>
		</thead>
		<tbody>
			{#each jobs as job}
				{@const gap = gapByJob[job.id]}
				<tr onclick={() => (location.href = `/jobs/${job.id}`)}>
					<td class="role">{job.title}</td>
					<td>{job.company}</td>
					<td>{job.seniority_level ?? '—'}</td>
					<td class="muted">{job.location}</td>
					{#if activeProfile.id}
						<td class="num">
							{#if gap}
								<span class="score" style="color:{scoreColor(gap.match_score)}">
									{Math.round(gap.match_score * 100)}%
								</span>
							{:else}
								<span class="muted">—</span>
							{/if}
						</td>
					{/if}
				</tr>
			{/each}
		</tbody>
	</table>
{/if}

<style>
	.ingest {
		display: flex;
		gap: 0.5rem;
		align-items: center;
		margin-bottom: 1.5rem;
	}
	.ingest input {
		flex: 1;
		padding: 0.6rem 0.75rem;
		background: #0d1117;
		border: 1px solid #30363d;
		border-radius: 6px;
		color: #e6edf3;
		font-size: 0.95rem;
	}
	.ingest button {
		padding: 0.6rem 1rem;
		background: #238636;
		border: none;
		border-radius: 6px;
		color: white;
		font-weight: 600;
		cursor: pointer;
	}
	.ingest button:disabled {
		opacity: 0.6;
		cursor: default;
	}
	.ingest-result {
		font-size: 0.85rem;
		color: #8b949e;
	}

	.hint {
		background: #161b22;
		border: 1px solid #30363d;
		border-radius: 6px;
		padding: 0.75rem 1rem;
		font-size: 0.9rem;
	}
	.hint a,
	.error a {
		color: #58a6ff;
	}

	table {
		width: 100%;
		border-collapse: collapse;
	}
	th {
		text-align: left;
		font-size: 0.8rem;
		text-transform: uppercase;
		letter-spacing: 0.04em;
		color: #8b949e;
		padding: 0.5rem 0.75rem;
		border-bottom: 1px solid #21262d;
	}
	th.num,
	td.num {
		text-align: right;
	}
	td {
		padding: 0.75rem;
		border-bottom: 1px solid #161b22;
		font-size: 0.95rem;
	}
	tbody tr {
		cursor: pointer;
	}
	tbody tr:hover {
		background: #161b22;
	}
	.role {
		font-weight: 600;
	}
	.score {
		font-weight: 700;
	}
	.muted {
		color: #8b949e;
	}
	.error {
		color: #f85149;
	}
</style>
