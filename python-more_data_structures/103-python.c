#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - prints Python bytes object info
 * @p: pointer to Python object
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t i, size, limit;
    char *str;

    printf("[.] bytes object info\n");

    if (strcmp(p->ob_type->tp_name, "bytes") != 0)
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = ((PyVarObject *)p)->ob_size;
    str = ((PyBytesObject *)p)->ob_sval;

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);

    limit = size + 1;
    if (limit > 10)
        limit = 10;

    printf("  first %ld bytes:", limit);
    for (i = 0; i < limit; i++)
        printf(" %02x", (unsigned char)str[i]);
    printf("\n");
}

/**
 * print_python_list - prints Python list information
 * @p: pointer to Python object
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t i, size, allocated;
    PyListObject *list;
    PyObject *item;

    list = (PyListObject *)p;
    size = ((PyVarObject *)p)->ob_size;
    allocated = list->allocated;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", allocated);

    for (i = 0; i < size; i++)
    {
        item = list->ob_item[i];
        printf("Element %ld: %s\n", i, item->ob_type->tp_name);

        if (strcmp(item->ob_type->tp_name, "bytes") == 0)
            print_python_bytes(item);
    }
}
