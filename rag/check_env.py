"""Phase 4, step 1: check that the RAG environment works.

Usage (from the RAG_sys folder, venv active):  python rag\check_env.py
Checks: Python version; packages import; Chroma's built-in local embedding model
        (all-MiniLM-L6-v2, about 80 MB, downloaded on first use) embeds and retrieves;
        one short test call to the Anthropic API.
The API key is read from the environment variable ANTHROPIC_API_KEY only; it is never printed.
Model: ANTHROPIC_MODEL environment variable, default claude-sonnet-5-5.
Exit code 1 if a check fails.
Flying Peptides training case. Fictitious manufacturer: Positive Climb Diagnostics.
"""
import os
import sys

MODEL = os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-5-5")
failed = False


def report(ok, label, detail=""):
    global failed
    failed |= not ok
    print(f"{'ok  ' if ok else 'FAIL'}  {label}{': ' + detail if detail else ''}")


# 1 Python
v = sys.version_info
report(v[:2] == (3, 11), "Python 3.11", f"{v.major}.{v.minor}.{v.micro} at {sys.executable}")
report(sys.prefix != sys.base_prefix, "running inside a venv", sys.prefix)

# 2 Packages
try:
    import chromadb, langchain_text_splitters, yaml, anthropic  # noqa: F401
    report(True, "packages import",
           f"chromadb {chromadb.__version__}, anthropic {anthropic.__version__}")
except ImportError as e:
    report(False, "packages import", f"{e} (run: pip install -r requirements.txt)")
    sys.exit(1)

# 3 Local embedding + retrieval (in memory, nothing written to disk)
try:
    client = chromadb.EphemeralClient()
    col = client.create_collection("env_check")
    col.add(ids=["a", "b"], documents=[
        "Raise a nonconformity record when a run fails system suitability.",
        "Integrate peaks in Skyline and export light to heavy ratios.",
    ])
    hit = col.query(query_texts=["Which software is used for peak integration?"], n_results=1)
    report(hit["ids"][0][0] == "b", "local embedding and retrieval",
           f"top hit = {hit['ids'][0][0]} (expected b)")
except Exception as e:
    report(False, "local embedding and retrieval", repr(e))

# 4 Anthropic API
if not os.environ.get("ANTHROPIC_API_KEY"):
    report(False, "ANTHROPIC_API_KEY set",
           "not found; set it as a Windows user environment variable and restart VS Code")
else:
    report(True, "ANTHROPIC_API_KEY set")
    try:
        resp = anthropic.Anthropic().messages.create(
            model=MODEL, max_tokens=20,
            messages=[{"role": "user", "content": "Reply with exactly: environment OK"}])
        text = "".join(b.text for b in resp.content if b.type == "text").strip()
        report("environment OK" in text, f"Anthropic call ({MODEL})",
               f"'{text}', {resp.usage.input_tokens} in / {resp.usage.output_tokens} out tokens")
    except anthropic.AuthenticationError:
        report(False, "Anthropic call", "key rejected (check for a typo or a revoked key)")
    except anthropic.NotFoundError:
        report(False, "Anthropic call", f"model '{MODEL}' not found; set ANTHROPIC_MODEL")
    except anthropic.APIError as e:
        report(False, "Anthropic call", f"{type(e).__name__}: {e}")

print("All checks passed." if not failed else "Some checks failed.")
sys.exit(1 if failed else 0)
