#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Prints information about a Python list
 * @p: Pointer to a PyObject (assumed to be a list)
 */
void print_python_list_info(PyObject *p)
{
  Py_ssize_t size, i;
  PyObject *item;
  PyListObject *list;

  printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));

  list = (PyListObject *)p;
  size = Py_SIZE(p);
  printf("[*] Allocated = %ld\n", list->allocated);

  for (i = 0; i < size; i++)
  {
    item = PyList_GetItem(p, i);
    printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
  }
}

int main(void)
{
  PyObject *l;

  Py_Initialize();
  l = PyList_New(0);

  PyList_Append(l, Py_BuildValue("s", "hello"));
  PyList_Append(l, Py_BuildValue("s", "World"));

  print_python_list_info(l);

  PyList_SetItem(l, 1, Py_BuildValue("s", "C is fun"));
  print_python_list_info(l);

  PyList_Append(l, Py_BuildValue("i", 42));
  PyList_Append(l, Py_BuildValue("f", 3.14159265359));
  print_python_list_info(l);

  PyList_SetItem(l, 2, Py_BuildValue("i", 98));
  print_python_list_info(l);

  PyList_Insert(l, 2, Py_BuildValue("f", 4.0));
  print_python_list_info(l);

  PyList_SetItem(l, 2, Py_BuildValue("(ii)", 98, 98));
  print_python_list_info(l);

  Py_DECREF(l);
  return (0);
}
