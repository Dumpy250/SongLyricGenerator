import os
import time
from openai import OpenAI

def get_lyrics(prompt: str, mode: str, max_tokens: int) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set. Add it to your Run Configuration env vars.")

    client = OpenAI(api_key=api_key)

    kind = "song lyrics" if mode == "song" else "poem"
    system = (
        f"You generate {kind}. Follow the user's prompt. "
        f"Format nicely with line breaks. "
        f"If it's a song, include verses and a chorus."
    )

    max_out = max(16, int(max_tokens))

    last_err = None
    for attempt in range(3):
        try:
            resp = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": prompt},
                ],
                max_tokens=max_out,
            )
            return resp.choices[0].message.content or ""
        except Exception as e:
            last_err = e
            time.sleep(0.5 * (2 ** attempt))

    raise last_err