from typing import Any

try:
    # langchain v1+ path
    from langchain.output_parsers import BaseOutputParser
except Exception:
    # fallback: define a minimal base class so parser still works if langchain isn't available
    class BaseOutputParser:
        def parse(self, text: str):
            raise NotImplementedError()


class StrOutputParser(BaseOutputParser):
    """A very small output parser that returns the raw string answer.

    Usage:
        parser = StrOutputParser()
        answer = parser.parse(llm_response.content)

    This keeps behavior simple and safe: it returns an empty string for None
    and strips leading/trailing whitespace.
    """

    def parse(self, text: str) -> str:
        if text is None:
            return ""
        return str(text).strip()

    def parse_with_prompt(self, text: str, prompt: Any) -> str:
        # langchain BaseOutputParser may call this; keep it consistent
        return self.parse(text)

    @property
    def _type(self) -> str:
        return "str"
