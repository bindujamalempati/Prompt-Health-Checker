
import re

# Direct toxicity rules
DIRECT_PATTERNS = {
    r"(rape|sexual assault|non-consensual|coercion|forced sex|molestation)": "Sexual violence reference",
    r"(violence|abuse).*sexual": "Sexual abuse context",
    r"(sex|intercourse).*without consent": "Non-consensual sexual context",
    r"(force|pressured|compelled).*sex": "Coerced sexual reference",
    r"email .*@.*": "PII: Email address requested",
    r"salary.*(over|above|below)": "PII: Salary range requested",
    r"female.*engineer|gender.*engineer": "Bias: Gender-specific professional filtering",
    r"ignore previous instructions": "Prompt injection attempt",
    r"pretend to be": "Prompt injection: role impersonation"
}

# Context-sensitive patterns
CONTEXTUAL_PATTERNS = {
    r"brutal (murder|attack|beating|rape)": "Violent act using 'brutal'",
    r"(killer|murderer|rapist) on the loose": "Criminal threat phrasing",
    r"insane (policy|decision|act)": "Insensitive term for mental health",
    r"crazy (rule|law|situation)": "Potentially offensive use of 'crazy'"
}

SAFE_PHRASES = [
    "brutal workout", "brutal schedule",
    "killer app", "killer idea",
    "crazy fun", "insane party"
]

def detect_contextual(prompt):
    prompt_lower = prompt.lower()
    for safe in SAFE_PHRASES:
        if safe in prompt_lower:
            return False, None
    for pattern, explanation in CONTEXTUAL_PATTERNS.items():
        if re.search(pattern, prompt, re.IGNORECASE):
            return True, explanation
    return False, None

def detect_direct(prompt):
    for pattern, explanation in DIRECT_PATTERNS.items():
        if re.search(pattern, prompt, re.IGNORECASE):
            return True, explanation
    return False, None

def smart_detect(prompt):
    direct, direct_reason = detect_direct(prompt)
    if direct:
        return "High", direct_reason
    context, context_reason = detect_contextual(prompt)
    if context:
        return "Medium", context_reason
    return "Low", None
