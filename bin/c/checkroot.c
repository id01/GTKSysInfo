// id01
// Checks for root access.
#include <unistd.h>
int main() { return setuid(0); }