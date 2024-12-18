#include <nanobind/nanobind.h>
#include <nanobind/stl/string.h>

namespace nb = nanobind;

using namespace nb::literals;


class Bird {
  std::string _name;
public:
  Bird(const std::string& name="Titi"): _name(name){}
  std::string speak(const std::string& translation={}) { return this->_name+ " says: cuicui (" + translation + ")"; }
};


NB_MODULE(nanobind_example_ext, m) {
    m.doc() = R"(This is a "hello world" example with nanobind.)";
    m.def("add", [](int a, int b) { return a + b; }, "a"_a, "b"_a, "Add two numbers.");

    nb::class_<Bird>(m, "Bird", R"(A cute little bird.

Example:
    >>> b = Bird()
    >>> b.speak('hello')
    'Titi says: cuicui (hello)'
)")
      .def(nb::init<const std::string&>(), "name"_a="Titi")
      .def("speak", &Bird::speak, "The bird speaks.")                        // basic binding
      .def("peep", &Bird::speak, "peep(text:str)->str \n\nThe bird peeps.")  // repeat prototype
      .def("tweet", &Bird::speak, "translation"_a, "The bird tweets.")       // named param
      ;
}
