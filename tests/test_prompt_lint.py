import sys
import unittest
import tempfile
import re
from pathlib import Path

# Add project root to sys.path to allow importing from scripts
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.prompt_lint import is_local_timecode, TIMECODE_RE, CHINESE_DIALOGUE_RE, FENCE_RE, lint_file


class TestPromptLint(unittest.TestCase):

    def test_is_local_timecode_valid(self):
        """Test is_local_timecode on valid timecode ranges."""
        # Simple mm:ss
        m1 = TIMECODE_RE.search("0:00 - 0:05")
        self.assertIsNotNone(m1)
        self.assertTrue(is_local_timecode(m1))

        # Leading zeros
        m2 = TIMECODE_RE.search("00:00 - 00:05")
        self.assertIsNotNone(m2)
        self.assertTrue(is_local_timecode(m2))

        # Exactly 15 seconds
        m3 = TIMECODE_RE.search("00:00 - 00:15")
        self.assertIsNotNone(m3)
        self.assertTrue(is_local_timecode(m3))

    def test_is_local_timecode_invalid(self):
        """Test is_local_timecode on invalid or long timecode ranges."""
        # Ends after 15 seconds
        m1 = TIMECODE_RE.search("00:00 - 00:16")
        self.assertIsNotNone(m1)
        self.assertFalse(is_local_timecode(m1))

        # Doesn't start at minute 0
        m2 = TIMECODE_RE.search("01:00 - 01:05")
        self.assertIsNotNone(m2)
        self.assertFalse(is_local_timecode(m2))

    def test_chinese_dialogue_re(self):
        """Test CHINESE_DIALOGUE_RE with standard, mixed, and invalid dialogue."""
        # Standard Chinese dialogue
        m1 = CHINESE_DIALOGUE_RE.search("“你好，我们去哪？”")
        self.assertIsNotNone(m1)
        self.assertEqual(m1.group("line"), "你好，我们去哪？")

        # Dialogue with English words
        m2 = CHINESE_DIALOGUE_RE.search("“这个 AIGC 的效果真好！”")
        self.assertIsNotNone(m2)
        self.assertEqual(m2.group("line"), "这个 AIGC 的效果真好！")

        # Dialogue with numbers and punctuation
        m3 = CHINESE_DIALOGUE_RE.search("“1，2，3，开始吧...！”")
        self.assertIsNotNone(m3)
        self.assertEqual(m3.group("line"), "1，2，3，开始吧...！")

        # No dialogue/English only (should not match if it lacks Chinese characters)
        m4 = CHINESE_DIALOGUE_RE.search("“Hello World”")
        self.assertIsNone(m4)

    def test_fence_re(self):
        """Test FENCE_RE matching capabilities for different MD structures."""
        # Standard fence block
        doc1 = (
            "### Segment 1 Seedance Prompt\n"
            "```text\n"
            "0:00-0:05: [S01] A man walks.\n"
            "```"
        )
        m1 = FENCE_RE.search(doc1)
        self.assertIsNotNone(m1)
        self.assertEqual(m1.group("title").strip(), "Segment 1 Seedance Prompt")
        self.assertEqual(m1.group("body").strip(), "0:00-0:05: [S01] A man walks.")

        # Blockquote inside the fence structure
        doc2 = (
            "### Segment 2 Seedance Prompt\n"
            "> Note here\n"
            "```text\n"
            "0:00-0:10: [S02] A dog runs.\n"
            "```"
        )
        m2 = FENCE_RE.search(doc2)
        self.assertIsNotNone(m2)
        self.assertEqual(m2.group("title").strip(), "Segment 2 Seedance Prompt")
        self.assertEqual(m2.group("body").strip(), "0:00-0:10: [S02] A dog runs.")

    def test_lint_file_valid_mock(self):
        """Test lint_file against a fully compliant mocked prompt file."""
        content = """# My AIGC Film

## Asset Design Prompts
- CHAR_HERO: "A realistic portrait of a man"

## Storyboard Prompts
### Segment 1 Storyboard
S01: Wide shot of a clean room.

### Segment 1 Seedance Prompt
```text
0:00 - 0:05: [S01] A man walks in CHAR_HERO.
禁止任何晃动和漂移，画面保持稳定。
不要字幕，无字幕，no subtitles.
```
"""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False, encoding="utf-8") as f:
            f.write(content)
            temp_path = Path(f.name)

        self.addCleanup(temp_path.unlink)

        results = lint_file(temp_path)
        # Should pass with no errors
        errors = [r for r in results if "exceeds" in r or "missing" in r or "ends after" in r]
        self.assertEqual(len(errors), 0, f"Lint failed with errors: {errors}")

    def test_lint_file_with_errors_mock(self):
        """Test lint_file correctly raises errors on non-compliant files."""
        # 1. Missing clean frame token
        # 2. Timecode ending after 15s
        content = """# My AIGC Film

## Asset Design Prompts
- CHAR_HERO: "A realistic portrait of a man"

## Storyboard Prompts
### Segment 1 Storyboard
S01: Wide shot of a clean room.

### Segment 1 Seedance Prompt
```text
0:00 - 0:20: [S01] A man walks in CHAR_HERO.
```
"""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False, encoding="utf-8") as f:
            f.write(content)
            temp_path = Path(f.name)

        self.addCleanup(temp_path.unlink)

        results = lint_file(temp_path)
        
        # Verify it catches the ends after 0:15 timecode error
        timecode_error = any("ends after 0:15" in r for r in results)
        self.assertTrue(timecode_error, "Should raise an error for timecode ending after 0:15")

        # Verify it catches the missing clean frame error
        clean_frame_error = any("missing clean-frame" in r for r in results)
        self.assertTrue(clean_frame_error, "Should raise an error for missing clean frame instruction")


if __name__ == "__main__":
    unittest.main()
