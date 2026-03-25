def compute_posterior_summary(posterior_samples):
    summary = {
        "critical_effort": compute_critical_effort(posterior_samples),
        "N0": compute_N0(posterior_samples),
        "r": compute_birth_rate(posterior_samples),
        "q": compute_catchability(posterior_samples),
    }
    return summary


def compute_critical_effort(posterior_samples):
    posterior_df = posterior_samples.copy()
    r = posterior_df["r"]
    q = posterior_df["q"]
    posterior_df["critical_effort"] = r / q
    return int(posterior_df.critical_effort.quantile(0.9).round(0))


def compute_N0(posterior_samples):
    return int(posterior_samples.N0.median().round(0))


def compute_birth_rate(posterior_samples):
    return posterior_samples.r.median()


def compute_catchability(posterior_samples):
    return posterior_samples.q.median()
