#AfterDojo
### The Args Kata
 
#HSLIDE

![CleanCode](http://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1436202607i/3735293._UY630_SR1200,630_.jpg)

#HSLIDE

> The arguments passed to the program consist of flags and values. Flags should be one character, preceded by a minus sign. Each flag should have zero, or one value associated with it.

#HSLIDE

> `./myprogram -l -p 8080 -d /usr/logs`


#HSLIDE

![](http://www.weteachwelearn.org/wp-content/uploads/2016/05/Discussion.jpg)

#HSLIDE

```python
class TestAcceptance(unittest.TestCase):
    def test_updates_parameter_values_from_command_line_arguments(self):
        
```

#HSLIDE

```python
class TestAcceptance(unittest.TestCase):
    def test_updates_parameter_values_from_command_line_arguments(self):
        parser = ArgParser(schema={"-l", ("-p", 8000), ("-b", "/usr/log")})
        parser.parse("-l -p 8080 -b /usr/local/log")
```

#HSLIDE

```python
class TestAcceptance(unittest.TestCase):
    def test_updates_parameter_values_from_command_line_arguments(self):
        parser = ArgParser(schema={"-l", ("-p", 8000), ("-b", "/usr/log")})
        parser.parse("-l -p 8080 -b /usr/local/log")
        self.assertEqual(parser.get("-l"), True)
        self.assertEqual(parser.get("-p"), 8080)
        self.assertEqual(parser.get("-b"), "/usr/local/log")
```

#HSLIDE
