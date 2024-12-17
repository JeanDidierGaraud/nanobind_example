#include <nanobind/nanobind.h>
#include <nanobind/stl/string.h>

namespace nb = nanobind;

using namespace nb::literals;


class Bird {
  std::string _name;
public:
  Bird(const std::string& name="Titi"): _name(name){}
  std::string speak(const std::string& prefix={}) { return this->_name+ " says: " + prefix + " cuicui"; }
};


NB_MODULE(nanobind_example_ext, m) {
    m.doc() = "This is a \"hello world\" example with nanobind.";
    m.def("add", [](int a, int b) { return a + b; }, "a"_a, "b"_a);

    nb::class_<Bird>(m, "Bird", "A genuine bird.")
      .def(nb::init<const std::string&>(), "name"_a="Titi")
      .def("speak", &Bird::speak, "The bird speaks.");
}

