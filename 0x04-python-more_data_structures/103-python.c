#define PY_SSIZE_T_CLEAN
#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

void print_python_list(PyObject *p)
{
  Py_ssize_t i;
  Py_ssize_t size = PyList_Size(p);

  printf("[*] Python list info\n");
  printf("[*] Size of the Python List = %ld\n", size);
  printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

  for (i = 0; i < size; i++)
  {
    printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
  }
}

void print_python_bytes(PyObject *p)
{
  Py_ssize_t size;
  char *string;
  Py_ssize_t i;

  printf("[.] bytes object info\n");
  printf("  size: %ld\n", PyBytes_Size(p));
  printf("  trying string: %s\n", PyBytes_AsString(p));

  size = PyBytes_Size(p);
  string = PyBytes_AsString(p);

  if (size >= 10)
  {
    printf("  first 10 bytes: ");
    for (i = 0; i < 10; i++)
    {
      printf("%02x%c", string[i] & 0xff, i < 9 ? ' ' : '\n');
    }
  }
  else
  {
    printf("  first %ld bytes: ", size);
    for (i = 0; i < size; i++)
    {
      printf("%02x%c", string[i] & 0xff, i < size - 1 ? ' ' : '\n');
    }
  }
}
