import unittest
from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

    def test_leaf_tag_value(self):
        node = LeafNode(
            "p",
            "this is some value text",
        )
        self.assertEqual(
            node.to_html(),
            "<p>this is some value text</p>"
        )

    def test_leaf_no_tag_value(self):
        node = LeafNode(
            None,
            "this is some value text",
        )
        self.assertEqual(
            node.to_html(),
            "this is some value text"
        )

    def test_leaf_with_props(self):
        node = LeafNode(
            "a",
            "this is some value text",
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.to_html(),
            '<a class="greeting" href="https://boot.dev">this is some value text</a>',
        )

    def test_leaf_value_error(self):
        node = LeafNode(
            None,
            None,
        )
        with self.assertRaises(ValueError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()
