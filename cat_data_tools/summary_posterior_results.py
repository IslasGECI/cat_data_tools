def compute_critical_effort(posterior_samples):
    r = posterior_samples["r"]
    q = posterior_samples["q"]
    posterior_samples.critical_effort = r / q
    return int(posterior_samples.critical_effort.quantile(0.9).round(0))
